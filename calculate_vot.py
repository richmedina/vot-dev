import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(message)s')

file_handler = logging.FileHandler('stop_tier.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


import os
import sys
import tempfile
import subprocess
import parselmouth
from praatio import tgio






def fileCheck(wav, TextGrid):

	wavName, wavExt = os.path.splitext(wav)
	textgridName, textgridExt = os.path.splitext(TextGrid)

	if wavExt != '.wav' or textgridExt != '.TextGrid':
		sys.exit("\n{} must be a wav file and {} must be a TextGrid file. "\
			"One or both files do not meet format requirements.\n".format(wav,TextGrid))
		# try:
		# 	sys.exit(...)
		# except SystemExit as e:
		# 	logger.error(str(e))
		# exit()
	else:
		print()
		logger.info("Processing {} and {}...\n".format(wav,TextGrid))

def processParameters(startPadding, endPadding, stops): 

	# adjust long padding values
	if startPadding > 0.025:
		logger.info("A startPadding of {} sec exceeds the maximum. It was adjusted to 0.025 sec.\n".format(startPadding))
		startPadding = 0.025
	elif startPadding < -0.025:
		logger.info("A startPadding of {} sec exceeds the minimum. It was adjusted to -0.025 sec.\n".format(startPadding))
		startPadding = -0.025
	if endPadding > 0.025:
		logger.info("An endPadding of {} sec exceeds the maximum. It was adjusted to 0.025 sec.\n".format(endPadding))
		endPadding = 0.025
	elif endPadding < -0.025:
		logger.info("An endPadding of {} sec exceeds the minimum. It was adjusted to -0.025 sec.\n".format(endPadding))
		endPadding = -0.025

	# specify stop categories
	ipaStops = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʔ', "p'", "t'", "k'", 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']
	voicelessStops = ['p', 't', 'ʈ', 'c', 'k', 'q', 'ʔ', "p'", "t'", "k'"]
	
	# define stops of interest
	if len(stops) == 0:
		stops = voicelessStops
	else:
		vettedStops, nonStops = [],[]
		for stopSymbol in stops:
			if stopSymbol.lower() in ipaStops:
				vettedStops.append(stopSymbol)
			else:
				nonStops.append(stopSymbol)

		if len(nonStops) == 1:
			logger.info("'{}' is not a stop sound. This symbol will be ignored in file {}.\n".format(nonStops[0],TextGrid))
		elif len(nonStops) > 1:
			logger.info("'{}' are not stop sounds. These symbols will be ignored in file {}.\n".format("', '".join(nonStops),TextGrid))

		if len(vettedStops) == 0:
			if len(stops) == 1:
				logger.warning("The sound you entered is not classified as a stop sound by the IPA.")
			elif len(stops) == 2:
				logger.warning("Neither of the sounds you entered is classified as a stop sound by the IPA.")
			else:
				logger.warning("None of the sounds you entered is classified as a stop sound by the IPA.")
			logger.info("The program will continue by analyzing all voiceless stops recognized by the IPA.\n")
			stops = voicelessStops
		else:
			stops = vettedStops
	return startPadding, endPadding, stops

def addStopTier(TextGrid, startPadding, endPadding, stops, outputPath):

	# open textgrid
	tg = tgio.openTextgrid(TextGrid)

	# verify that no 'AutoVOT' or 'stops' tiers exist
	for tierName in tg.tierNameList:
		if tierName == "AutoVOT":
			logger.warning("A tier named 'AutoVOT' already exists. Said tier will be renamed as 'autovot - original' to avoid a naming conflict.\n")
			tg.renameTier("AutoVOT", "autovot - original")
		elif tierName[-5:] == 'stops':
			sys.exit("Error: There is a tier with the word 'stops' in its label in {}. You must relabel said tier before continuing.".format(TextGrid))
	
	# convert tier labels to lowercase
	tg.tierNameList = [tierName.lower() for tierName in tg.tierNameList]
	tg.tierDict = dict((k.lower(), v) for k, v in tg.tierDict.items())

	# remove directory from TG name
	TextGrid = TextGrid.split("/")[1] #delete

	# collect all word tiers and terminate process if none exists
	allWordTiers = [tierName for tierName in tg.tierNameList if 'word' in tierName]
	if len(allWordTiers) == 0:
		sys.exit("Error: {} does not contain any tier labeled 'words'.\n".format(TextGrid))

	# collect all phone tiers and terminate process if none exists
	allPhoneTiers = [tierName for tierName in tg.tierNameList if 'phone' in tierName]
	if len(allPhoneTiers) == 0:
		sys.exit("Error: {} does not contain any tier labeled 'phones'.\n".format(TextGrid))
		# try:
		# 	sys.exit("Error: {} does not contain any tier labeled 'phones'.\n".format(TextGrid))
		# except SystemExit as e:
		# 	logger.error(str(e))
		# exit()

	# verify that an equal number of word and phone tiers exists before continuing
	if len(allWordTiers) == len(allPhoneTiers):

		# add stop tier
		voicedTokens =[]
		totalSpeakers = len(allPhoneTiers)
		currentSpeaker = 0
		lastSpeaker =	False
		populatedTiers = 0

		for tierName in allPhoneTiers:
			currentSpeaker += 1
			if tierName.replace('phone', 'word') in allWordTiers:
				speakerName = tierName.split("phone")[0]
				phoneTier = tg.tierDict[tierName]
				wordTier = tg.tierDict[tierName.replace('phone','word')]
				wordStartTimes = [entry[0] for entry in wordTier.entryList]
				if totalSpeakers == currentSpeaker:
					lastSpeaker = True
				newTier = processStopTier(
						phoneTier, 
						stops, 
						wordStartTimes, 
						voicedTokens, 
						startPadding, 
						endPadding, 
						TextGrid, 
						lastSpeaker, 
						speakerName
						)
				if newTier:
					tg.addTier(newTier)
					populatedTiers += 1
				else:
					continue
			
			else:
				sys.exit("Error: The names of the 'word' and 'phone' tiers are inconsistent in file {}. "\
					"Fix the issue before continuing.\n".format(TextGrid))
	
	else:
		sys.exit("Error: There isn't an even number of 'phone' and 'word' tiers per speaker in file {}. "\
			"Fix the issue before continuing.\n".format(TextGrid))

	if populatedTiers == 0:
		sys.exit("Error: There were no voiceless stops found in {}.\n".format(TextGrid))

	# generate list of all stop tiers created
	stopTiers = [tierName for tierName in tg.tierNameList if tierName[-5:] == "stops"]

	# save the new textgrid with a 'stop' tier
	saveName = TextGrid.split(".TextGrid")[0]+"_output.TextGrid"
	tg.save(os.path.join(outputPath,saveName),useShortForm=False)
	
	return stopTiers, saveName

def processStopTier(
	phoneTier, 
	stops, 
	wordStartTimes, 
	voicedTokens, 
	startPadding, 
	endPadding, 
	TextGrid, 
	lastSpeaker, 
	speakerName
	):

	# specify voiced stops
	voicedStops = ['b', 'd', 'ɖ', 'ɟ', 'g', 'ɢ', 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']

	# gather stops of interest from TextGrid
	stopEntryList = []
	for entry in phoneTier.entryList:
		if entry[-1].lower() in stops and entry[0] in wordStartTimes:
			stopEntryList.append(entry)
			if entry[-1].lower() in voicedStops:
				voicedTokens.append(entry[-1].lower())

	# apply padding and convert phone labels to lowercase
	extendedEntryList = []
	for start, stop, label in stopEntryList:
		extendedEntryList.append([start+startPadding, stop+endPadding, label.lower()])

	# check for and resolve length requirements and timing conflicts
	for interval in range(len(extendedEntryList)-1):
		currentPhone = extendedEntryList[interval]
		nextPhone = extendedEntryList[interval+1]
		startTime, endTime = 0, 1

		if currentPhone[endTime] > nextPhone[startTime]:  # check if there is an overlap between phones
			sys.exit("Error: In file {} (after adding padding), the segment starting at {} sec overlaps with the segment starting at {}."\
			"\nYou might have to decrease the amount of padding and/or manually adjust segmentation to solve the conflicts."\
			"\n\nProcess incomplete.\n".format(TextGrid, round(currentPhone[startTime],3), round(nextPhone[startTime],3))) #how to do sys.exit()??
		elif currentPhone[endTime] - currentPhone[startTime] < 0.025:  # check if currentPhone is under 25ms
			if nextPhone[startTime] - currentPhone[endTime] <= 0.020:  # check if nextPhone is within 20ms
				currentPhone[endTime] = currentPhone[startTime] + 0.025  # make currentPhone 25ms long
				nextPhone[startTime] = currentPhone[endTime] + 0.021  # shift nextPhone 21ms after new endTime of currentPhone
				logger.warning("In File {}, the phone starting at {} was elongaged to 25 ms because it did not meet length "\
					"requirements, and the phone starting at {} was shifted forward due to a proximity issue. "\
					"Please, verify manually that the modified windows still capture the segments accurately.\n"\
					.format(TextGrid,round(currentPhone[startTime],3),round(nextPhone[startTime],3)))
			else:
				currentPhone[endTime] = currentPhone[startTime] + 0.025  # make currentPhone 25ms long
				logger.warning("In File {}, the phone starting at {} was elongaged to 25 ms because it did not meet length "\
					"requirements.\n"\
					.format(TextGrid,round(currentPhone[startTime],3)))
		else:
			if nextPhone[startTime] - currentPhone[endTime] <= 0.020:  # check if nextPhone is within 20ms
				nextPhone[startTime] = currentPhone[endTime] + 0.021  # shift nextPhone 21ms after endTime of currentPhone
				logger.warning("In File {}, the phone starting at {} was shifted forward due to a proximity issue.\n"\
						.format(TextGrid,round(nextPhone[startTime],3)))

		if interval == len(extendedEntryList)-1 and nextPhone[endTime] - nextPhone[startTime] < 0.025:  # if the last segment is too short
			nextPhone[endTime] = nextPhone[startTime] + 0.025  # shift nextPhone's (last phone) endTime to be 25 ms after startTime

	# provide warning for voiced tokens
	if len(list(set(voicedTokens))) == 1 and lastSpeaker:  # check for lastSpeaker to print info only once, if multiple speakers are present
		logger.warning("You're trying to obtain VOT calculations of the following voiced stop: '{}'".format(*list(set(voicedTokens)))) # best way to list??
		logger.info("Note that AutoVOT's current model only works on voiceless stops; "\
			"prevoicing in the productions may result in inaccurate calculations.\n")
	elif len(list(set(voicedTokens))) > 1 and lastSpeaker:  # check for lastSpeaker to print info only once, if multiple speakers are present
		logger.warning("You're trying to obtain VOT calculations of the following voiced stops: '{}'".format("', '".join(list(set(voicedTokens)))))
		logger.info("Note that AutoVOT's current model only works on voiceless stops; "\
			"prevoicing in the productions may result in inaccurate calculations.\n")

	# construct the stop tier if stops were identified
	if len(extendedEntryList) > 0:
		stopTier = phoneTier.new(name = speakerName+"stops", entryList = extendedEntryList)
		return stopTier		
	else:
		return False

def applyAutoVOT(wav, stopTiers, annotatedTextgrid):

	# make temporary directory to process predictions
	with tempfile.TemporaryDirectory() as tempDirectory:

		# process the sound file
		psnd = parselmouth.Sound(wav)
		tempSound = os.path.join(tempDirectory,wav)
		if psnd.get_sampling_frequency() != 16000:
			psnd = psnd.resample(16000)
			if psnd.get_number_of_channels() != 1:
				psnd = psnd.extract_channel(1)
		else:
			if psnd.get_number_of_channels() != 1:
				psnd = psnd.extract_channel(1)
		psnd.save(tempSound, "WAV")
		
		# run VOT predictor
		for tierName in stopTiers:
			subprocess.run([
				'python', 'autovot_shortcut/auto_vot_decode.py', 
				'--vot_tier', tierName,
				'--vot_mark', '*', 
				tempSound, 
				annotatedTextgrid, 
				'autovot_shortcut/models/vot_predictor.amanda.max_num_instances_1000.model',
				'--ignore_existing_tiers'
				])

	# rename repeated labels of AutoVOT prediction tiers
	if len(stopTiers) > 1:  # if multiple speakers
		with open(annotatedTextgrid, "r") as TG:
			newTG = []
			tierNumber = 0
			for line in TG:
				if "AutoVOT" in line:
					line = line.replace("AutoVOT",stopTiers[tierNumber].split("stops")[0]+"AutoVOT") # relies on naming of tiers as "stops"
					tierNumber += 1
				newTG.append(line)
		with open(annotatedTextgrid, "w") as TG:
			TG.writelines(newTG)
	return

def calculateVOT(wav, TextGrid, stops=[], outputDirectory='output', startPadding=0, endPadding=0):

	# verify file format
	fileCheck(wav, TextGrid)

	# process variable parameters
	startPadding, endPadding, stops = processParameters(startPadding, endPadding, stops)

	# create directory to output files
	outputPath = os.path.join(os.getcwd(),outputDirectory)
	if not os.path.exists(outputPath):
		os.mkdir(outputPath)

	# add stop tier populated with tokens of interest
	stopTiers, saveName = addStopTier(TextGrid, startPadding, endPadding, stops, outputPath)
	
	# specify where the annotated TG is located 
	annotatedTextgrid = os.path.join(outputDirectory, saveName)

	# apply AutoVOT prediction calculations
	applyAutoVOT(wav, stopTiers, annotatedTextgrid)

	logger.info("Process for {} and {} is complete.\n".format(wav,TextGrid))

	return

# calculateVOT("test.wav", "testing/test14.TextGrid")

# if __name__ == '__main__':
# 	unittest.main()










