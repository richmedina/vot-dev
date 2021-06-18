import os
from praatio import tgio

def addStopTier(TextGrid, stops=[], startPadding=0, endPadding=0):

	# open textgrid and turn the tier labels to lowercase strings
	tg = tgio.openTextgrid(TextGrid)
	tg.tierNameList = [tier.lower() for tier in tg.tierNameList]
	tg.tierDict = dict((k.lower(), v) for k, v in tg.tierDict.items())

	# collect all word tiers and terminate process if none exists
	allWordTiers = [tierName for tierName in tg.tierNameList if 'word' in tierName]
	if len(allWordTiers) == 0:
		print(TextGrid,"does not contain any tier named 'Words'.\n")
		return False #return False

	# collect all phone tiers and terminate process if none exists
	allPhoneTiers = [tierName for tierName in tg.tierNameList if 'phone' in tierName]
	if len(allPhoneTiers) == 0:
		print(TextGrid,"does not contain any tier named 'Phones'.\n")
		return False #return False

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
						populatedTiers, 
						startPadding, 
						endPadding, 
						voicedTokens, 
						lastSpeaker
						)
				if newTier:
					populatedTiers += 1
					tg.addTier(newTier)
				else:
					continue
			
			else:
				print("The names of the 'word' and 'phone' tiers are inconsistent in file",\
					TextGrid+".","Fix the issue before continuing.\n")
				return False #return False
	
	else:
		print("Error: There isn't an even number of 'phone' and 'word' tiers per speaker in file",\
			TextGrid,". Fix the issue before continuing.\n")
		return False #return False

	# save the new textgrid with a 'stop' tier
	saveName = TextGrid.split(".TextGrid")[0]
	tg.save(saveName+"_output.TextGrid") #add output directory to store temp tg?
	
	return


def processStopTier(TextGrid, speakerName, phoneTier, wordStartTimes, stops, populatedTiers, startPadding, endPadding, voicedTokens, lastSpeaker): 

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
		extendedEntryList.append([start+startPadding, stop+endPadding, label])

	# check for length requirements and resolve overlapping conflicts
	for interval in range(len(extendedEntryList)-1):
		#intA = current interval
		#intB = next interval
		if extendedEntryList[interval][1]-extendedEntryList[interval][0] < 0.025:
			extendedEntryList[interval][1] = extendedEntryList[interval][0] + 0.025
			if extendedEntryList[interval+1][0] < extendedEntryList[interval][1]:
				if extendedEntryList[interval+1][0] - extendedEntryList[interval][1] > 0.075:
					print("Error: there is a significant overlap between two phone segments at time:",\
						extendedEntryList[interval][1],"in file:",TextGrid,". Fix the issue before continuing.\n")
					#stop function -- too big of a shift
				# 	return # sys.exit()
				# print("Error: There are two segments in file:",TextGrid,"around time:",extendedEntryList[interval][1],\
				# 	"that either overlap with each other, or are too short to calculate VOT. Fix the issue before continuing.")
				# print("This could be an issue resulting from:"\
				# 	"\n(1) very fast speech, \n(2) two tokens very close to each other, or \n(3) too much 'padding'.\n")
				# #stop function -- too much of an overlap
				return
			else:
				print("Note: the segment in file:",TextGrid,"at time:",extendedEntryList[interval][0],\
				"was automatically elongated because it was shorter than the required 25 ms.\n")
		if extendedEntryList[interval+1][0] < extendedEntryList[interval][1]:
			extendedEntryList[interval+1][0] = extendedEntryList[interval][1]
			print("Note: the start time for the segment in file:",TextGrid,"at time:",extendedEntryList[interval+1][0],\
				"was shifted back to resolve an issue with overlapping segments.")
			print("The issue with overlapping times could be an issue resulting from:",\
				"\n(1) very fast speech, \n(2) two tokens very close to each other, or \n(3) too much 'padding'.\n")

	# provide warning for voiced tokens
	if len(voicedTokens) > 0 and lastSpeaker:
		print("***Warning: You're trying to obtain VOT calculations of the following voiced stops: ",list(set(voicedTokens)))
		print("Note that AutoVOT's current model only works on voiceless stops; "\
			"prevoicing in the productions may result in inaccurate calculations.\n")

	# construct the stop tier if stops were identified
	if len(extendedEntryList) > 0:
		stopTier = phoneTier.new(name = speakerName+"stops", entryList = extendedEntryList)
		return stopTier
	elif lastSpeaker and populatedTiers == 0:
		print("There were no voiceless stops found in",TextGrid+".\n")
		return False
	else:
		return

addStopTier('test1.1.TextGrid')








