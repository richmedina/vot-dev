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


from praatio import tgio
from os.path import join
import os
import sys


def addStopTier(TextGrid, outputPath, stops, startPadding, endPadding):

	# open textgrid, turn the tier labels to lowercase strings, verify that no 'stops' tier exists
	tg = tgio.openTextgrid(TextGrid)
	for tierName in tg.tierNameList:
		if tierName == "AutoVOT":
			logger.warning(" A tier named 'AutoVOT' already exists. Said tier will be renamed as 'autovot - original' to avoid a naming conflict.\n")
			tg.renameTier("AutoVOT", "AutoVOT - original")
		elif tierName[-5:] == 'stops':
			sys.exit("There is a tier with the word 'stops' in {}. You must relabel said tier before continuing.".format(TextGrid))
	tg.tierNameList = [tierName.lower() for tierName in tg.tierNameList]
	tg.tierDict = dict((k.lower(), v) for k, v in tg.tierDict.items())

	# remove directory from TG name
	TextGrid = TextGrid.split("/")[1] #delete

	# collect all word tiers and terminate process if none exists
	allWordTiers = [tierName for tierName in tg.tierNameList if 'word' in tierName]
	if len(allWordTiers) == 0:
		sys.exit("Error:{} does not contain any tier named 'words'.\n".format(TextGrid))

	# collect all phone tiers and terminate process if none exists
	allPhoneTiers = [tierName for tierName in tg.tierNameList if 'phone' in tierName]
	if len(allPhoneTiers) == 0:
		sys.exit("Error:{} does not contain any tier named 'phones'.\n".format(TextGrid))

	# verify that an equal number of word and phone tiers exists before continuing
	if len(allWordTiers) == len(allPhoneTiers):

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
						TextGrid, 
						speakerName, 
						phoneTier, 
						wordStartTimes, 
						stops, 
						startPadding, 
						endPadding, 
						voicedTokens, 
						currentSpeaker, 
						lastSpeaker
						)
				if newTier:
					populatedTiers += 1
					tg.addTier(newTier)
				else:
					continue
			
			else:
				sys.exit("Error:The names of the 'word' and 'phone' tiers are inconsistent in file {}. Fix the issue before continuing.\n".format(TextGrid))
	
	else:
		sys.exit("Error:There isn't an even number of 'phone' and 'word' tiers per speaker in file {}. Fix the issue before continuing.\n".format(TextGrid))

	if populatedTiers == 0:
		sys.exit("Error:There were no voiceless stops found in {}.\n".format(TextGrid))
	stopTiers = [tierName for tierName in tg.tierNameList if tierName[-5:] == "stops"]

	# save the new textgrid with a 'stop' tier
	saveName = TextGrid.split(".TextGrid")[0]+"_output.TextGrid"
	tg.save(os.path.join(outputPath,saveName),useShortForm=False)
	
	return stopTiers, saveName, (totalSpeakers > 1)

def processStopTier(
	TextGrid, 
	speakerName, 
	phoneTier, 
	wordStartTimes, 
	stops, 
	startPadding, 
	endPadding, 
	voicedTokens, 
	currentSpeaker, 
	lastSpeaker
	): 

	# adjust long padding values
	if startPadding > 0.025:
		logger.info("A startPadding of {} sec exceeds the maximum. It was adjusted to 0.025 sec.".format(startPadding))
		startPadding = 0.025
	elif startPadding < -0.025:
		logger.info("A startPadding of {} sec exceeds the minimum. It was adjusted to -0.025 sec.".format(startPadding))
		startPadding = -0.025
	if endPadding > 0.025:
		logger.info("An endPadding of {} sec exceeds the maximum. It was adjusted to 0.025 sec.".format(endPadding))
		endPadding = 0.025
	elif endPadding < -0.025:
		logger.info("An endPadding of {} sec exceeds the minimum. It was adjusted to -0.025 sec.".format(endPadding))
		endPadding = -0.025

	# specify stop categories
	ipaStops = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʔ', "p'", "t'", "k'", 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']
	voicelessStops = ['p', 't', 'ʈ', 'c', 'k', 'q', 'ʔ', "p'", "t'", "k'"]
	voicedStops = ['b', 'd', 'ɖ', 'ɟ', 'g', 'ɢ', 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']

	# define stops of interest
	if len(stops) == 0: # move these outside of this func?
		stops = voicelessStops
	else:
		vettedStops, nonStops = [],[]
		for stopSymbol in stops:
			if stopSymbol.lower() in ipaStops:
				vettedStops.append(stopSymbol)
			else:
				nonStops.append(stopSymbol)

		if len(nonStops) == 1 and currentSpeaker == 1: # move these outside of this func?
			logger.info("'{}' is not a stop sound. This symbol will be ignored in file {}.\n".format(nonStops[0],TextGrid))
		elif len(nonStops) > 1 and currentSpeaker == 1:
			logger.info("'{}' are not stop sounds. These symbols will be ignored in file {}.\n".format(", ".join(nonStops),TextGrid))

		if len(vettedStops) == 0 and currentSpeaker == 1: # move these outside of this func?
			if len(stops) == 1:
				logger.warning("The only sound you entered is not classified as a stop sound by the IPA.") # move these outside of this func?
			elif len(stops) == 2:
				logger.warning("Neither of the sounds you entered is classified as a stop sound by the IPA.")
			else:
				logger.warning("None of the sounds you entered is classified as a stop sound by the IPA.")
			logger.info("The program will continue by analyzing all voiceless stops recognized by the IPA.\n")
			stops = voicelessStops
		else:
			stops = vettedStops

	# identify stops of interest in the TextGrid
	stopEntryList = []
	for entry in phoneTier.entryList:
		if entry[-1].lower() in stops and entry[0] in wordStartTimes:
			stopEntryList.append(entry)
			if entry[-1].lower() in voicedStops:
				voicedTokens.append(entry[-1].lower())

	# apply padding
	extendedEntryList = []
	for start, stop, label in stopEntryList:
		extendedEntryList.append([start+startPadding, stop+endPadding, label.lower()])

	# check for and resolve length requirements and timing conflicts
	for interval in range(len(extendedEntryList)-1):
		currentPhone = extendedEntryList[interval]
		nextPhone = extendedEntryList[interval+1]
		startTime, endTime = 0, 1

		if currentPhone[endTime] > nextPhone[startTime]:  # check if there is an overlap
			# try:
			sys.exit("Error:In file {}, after adding padding, the segment starting at {} sec overlaps with the segment starting at {}."\
			"\nYou might have to decrease the amount of padding and/or manually adjust segmentation to solve the conflicts."\
			"\n\nProcess incomplete.\n".format(TextGrid, round(currentPhone[startTime],3), round(nextPhone[startTime],3))) #how to do sys.exit()??
		elif currentPhone[endTime] - currentPhone[startTime] < 0.025:  # check if currentPhone is under 25ms
			if nextPhone[startTime] - currentPhone[endTime] <= 0.020:  # check if nextPhone is within 20ms
				currentPhone[endTime] = currentPhone[startTime] + 0.025  # make currentPhone 25ms long
				nextPhone[startTime] = currentPhone[endTime] + 0.021  # shift nextPhone 21ms after new endTime of currentPhone
				logger.warning("In File {}, the phone starting at {} was elongaged to 25 ms because it did not meet length "\
					"requirements, and the phone starting at {} was shifter forward due to a proximity issue. "\
					"Please, verify manually that the modified windows still captures the segments accurately."\
					.format(TextGrid,round(currentPhone[startTime],3),round(nextPhone[startTime],3)))
			else:
				currentPhone[endTime] = currentPhone[startTime] + 0.025  # make currentPhone 25ms long
				logger.warning("In File {}, the phone starting at {} was elongaged to 25 ms because it did not meet length "\
						"requirements."\
						.format(TextGrid,round(currentPhone[startTime],3)))
		else:
			if nextPhone[startTime] - currentPhone[endTime] <= 0.020:  # check if nextPhone is within 20ms
				nextPhone[startTime] = currentPhone[endTime] + 0.021  # shift nextPhone 21ms after new endTime of currentPhone
				logger.warning("In File {}, the phone starting at {} was shifted forward due to a proximity issue."\
						.format(TextGrid,round(nextPhone[startTime],3)))

		if interval == len(extendedEntryList)-1 and nextPhone[endTime] - nextPhone[startTime] < 0.025:  # if the last segment is too short
			nextPhone[endTime] = nextPhone[startTime] + 0.025  # shift currentPhone's endTime to be 25 ms after startTime

	# provide warning for voiced tokens
	if len(list(set(voicedTokens))) == 1 and lastSpeaker:
		logger.warning(" You're trying to obtain VOT calculations of the following voiced stop: '{}'".format(*list(set(voicedTokens))))
		logger.info("Note that AutoVOT's current model only works on voiceless stops; "\
			"prevoicing in the productions may result in inaccurate calculations.\n")
	elif len(list(set(voicedTokens))) > 1 and lastSpeaker:
		logger.warning("You're trying to obtain VOT calculations of the following voiced stops: '{}'".format("', '".join(list(set(voicedTokens)))))
		logger.info("Note that AutoVOT's current model only works on voiceless stops; "\
			"prevoicing in the productions may result in inaccurate calculations.\n")

	# construct the stop tier if stops were identified
	if len(extendedEntryList) > 0:
		stopTier = phoneTier.new(name = speakerName+"stops", entryList = extendedEntryList)
		return stopTier		
	else:
		return False

# addStopTier('test1.TextGrid')








