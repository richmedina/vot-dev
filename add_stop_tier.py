import os
from praatio import tgio

def addStopTier(TextGrid, stops=[], startPadding=0, endPadding=0):

	fileCheck(TextGrid) #??

	# open textgrid and turn the tier labels to lowercase strings
	tg = tgio.openTextgrid(TextGrid)
	tg.tierNameList = [tier.lower() for tier in tg.tierNameList]
	tg.tierDict = dict((k.lower(), v) for k, v in tg.tierDict.items())

	# collect all word tiers and terminate process if none exists
	allWordTiers = [tierName for tierName in tg.tierNameList if 'word' in tierName]
	if len(allWordTiers) == 0:
		print("This TextGrid file does not contain a tier named 'Words'.\n")
		return

	# collect all phone tiers and terminate process if none exists
	allPhoneTiers = [tierName for tierName in tg.tierNameList if 'phone' in tierName]
	if len(allPhoneTiers) == 0:
		print("This TextGrid file does not contain a tier named 'Phones'.\n")
		return

	# verify that an equal number of word and phone tiers exists to continue
	if len(allWordTiers) == len(allPhoneTiers):

		voicedTokens =[]
		totalSpeakers = len(allPhoneTiers)
		currentSpeaker = 0
		voicedWarning =	False

		for tier in allPhoneTiers:
			currentSpeaker += 1
			if 'phone' in tier and tier.replace('phone', 'word') in allWordTiers:
				speakerName = tier.split("phone")[0]
				phoneTier = tg.tierDict[tier]
				wordTier = tg.tierDict[tier.replace('phone','word')]
				wordStartTimes = [entry[0] for entry in wordTier.entryList]
				if totalSpeakers == currentSpeaker:
					voicedWarning = True
				tg.addTier(
					processStopTier(
						TextGrid, 
						speakerName, 
						phoneTier, 
						wordStartTimes, 
						stops, 
						startPadding, 
						endPadding, 
						voicedTokens, 
						voicedWarning
						)
					)
			
			else:
				print("The names of the 'word' and 'phone' tiers are inconsistent in file",TextGrid+".","Fix the issue before continuing.\n")
				return
				#stop
	else:
		print("Error: There isn't an even number of 'phone' and 'word' tiers per speaker in file",TextGrid,". Fix the issue before continuing.\n")
		return
		#stop

	# save the new textgrid with a 'stop' tier
	saveName = TextGrid.split(".TextGrid")[0]
	tg.save(saveName+"_output.TextGrid")
	
	return


def processStopTier(TextGrid, speakerName, phoneTier, wordStartTimes, stops, startPadding, endPadding, voicedTokens, voicedWarning): 

	# specify stop categories
	ipaStops = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʔ', "p'", "t'", "k'", 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']
	voicelessStops = ['p', 't', 'ʈ', 'c', 'k', 'q', 'ʔ', "p'", "t'", "k'"]
	voicedStops = ['b', 'd', 'ɖ', 'ɟ', 'g', 'ɢ', 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']

	# define stops of interest
	if len(stops) == 0:
		stops = voicelessStops
	else:
		tempStops = []
		for stopSymbol in stops:
			if stopSymbol.lower() in ipaStops:
				tempStops.append(stopSymbol)
			else:
				print("'"+stopSymbol+"'","is not a stop sound. This symbol will be ignored.\n")
		stops = tempStops

	# identify stops of interest
	stopEntryList = []
	for entry in phoneTier.entryList:
		if entry[-1].lower() in stops and entry[0] in wordStartTimes:
			stopEntryList.append(entry)
			if entry[-1].lower() in voicedStops:
				voicedTokens.append(entry[-1].lower())

	# apply padding
	extendedEntryList = []
	for start, stop, label in stopEntryList:
		extendedEntryList.append([start+startPadding, stop+endPadding, label])

	# check for length requirements and resolve overlapping conflicts
	fileName = TextGrid
	for interval in range(len(extendedEntryList)-1):
		if extendedEntryList[interval][1]-extendedEntryList[interval][0] < 0.025:
			extendedEntryList[interval][1] = extendedEntryList[interval][0] + 0.025
			if extendedEntryList[interval+1][0] < extendedEntryList[interval][1]:
				if extendedEntryList[interval+1][0] - extendedEntryList[interval][1] > 0.075:
					print("Error: there is a significant overlap between two phone segments at time:",\
						extendedEntryList[interval][1],"in file:",fileName,". Fix the issue before continuing.\n")
					#stop function -- too big of a shift
				print("Error: There are two segments in file:",fileName,"around time:",extendedEntryList[interval][1],\
					"that either overlap with each other, or are too short to calculate VOT. Fix the issue before continuing.")
				print("This could be an issue resulting from:"\
					"\n(1) very fast speech, \n(2) two tokens very close to each other, or \n(3) too much 'padding'.\n")
				#stop function -- too much of an overlap
				return
			else:
				print("Note: the segment in file:",fileName,"at time:",extendedEntryList[interval][0],\
				"was automatically elongated because it was shorter than the required 25 ms.\n")
		if extendedEntryList[interval+1][0] < extendedEntryList[interval][1]:
			extendedEntryList[interval+1][0] = extendedEntryList[interval][1]
			print("Note: the start time for the segment in file:",fileName,"at time:",extendedEntryList[interval+1][0],\
				"was shifted back to resolve an issue with overlapping segments.")
			print("The issue with overlapping times could be an issue resulting from:",\
				"\n(1) very fast speech, \n(2) two tokens very close to each other, or \n(3) too much 'padding'.\n")

	# provide warning for voiced tokens
	if len(voicedTokens) > 0 and voicedWarning:
		print("***Warning: You're trying to obtain VOT calculations of the following voiced stops: ",list(set(voicedTokens)),".")
		print("Note that AutoVOT's current model only works on voiceless stops; "\
			"prevoicing in the productions may result in inaccurate calculations.\n")

	# construct the stop tier
	stopTier = phoneTier.new(name = speakerName+"stops", entryList = extendedEntryList)

	return stopTier

def fileCheck(TextGrid):
	name, ext = os.path.splitext(TextGrid)
	if ext != '.TextGrid':
		print(TextGrid,"is not a .TextGrid file.\n")
		#add stop to the entire program
	else:
		print("All is good with the format of file",TextGrid,"\n")
		return


addStopTier('test1.TextGrid',['k','b','g'])








