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
					TextGrid+". Fix the issue before continuing.\n")
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
	if len(stops) == 0: # move these outside of this func?
		stops = voicelessStops
	else:
		vettedStops, nonStops = [],[]
		for stopSymbol in stops:
			if stopSymbol.lower() in ipaStops:
				vettedStops.append(stopSymbol)
			else:
				nonStops.append(stopSymbol)

		if len(nonStops) == 1: # move these outside of this func?
			print("'"+nonStops[0]+"' is not a stop sound. This symbol will be ignored.\n")
		elif len(nonStops) > 1:
			print("'"+", ".join(nonStops)+"'","are not stop sounds. These symbols will be ignored for file",TextGrid+".\n")

		if len(vettedStops) == 0: # move these outside of this func?
			if len(stops) == 1:
				print("The sound you entered is not considered a stop sound by the IPA.") # move these outside of this func?
			elif len(stops) == 2:
				print("Neither of the sounds you entered is considered a stop sound by the IPA.")
			else:
				print("None of the sounds you entered is considered a stop sound by the IPA.")
			print("The program will continue by analyzing all voiceless stops recognized by the IPA.\n")
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
		extendedEntryList.append([start+startPadding, stop+endPadding, label])

	# check for and resolve length requirements and timing conflicts
	for interval in range(len(extendedEntryList)-1):
		currentPhone = extendedEntryList[interval]
		nextPhone = extendedEntryList[interval+1]
		startTime, endTime = 0, 1

		if currentPhone[endTime] > nextPhone[startTime]:  # if nextPhone starts before currentPhone ends, there's an overlap
			if currentPhone[endTime] - currentPhone[startTime] < 0.025:  # each phone window must be at least 25 ms in length
				if currentPhone[endTime] - nextPhone[startTime] > 50:
					print("Error: in file",TextGrid+",","the segment starting at",currentPhone[startTime],"sec shows two timing conflicts:",\
						"\n(1) it is shorter than 25 ms. \n(2) it overlaps with the segment starting at",nextPhone[startTime]+".",\
						"\nYou migh have to decrease the amount of padding and/or manually increase the segment length to solve the conflicts.")
					sys.exit() ## check out this termination method ?
				else:
					nextPhone[startTime] = currentPhone[endTime]
					print("Warning: in file",TextGrid+",","the segment starting at",nextPhone[startTime],"sec was shifted forward to resolve a",\
						"timing conflict (two overlapping segment). Please, verify manually that the shifted window still captures the segment.")
			else:
				if currentPhone[endTime] - nextPhone[startTime] > 50:
					print("Error: in file",TextGrid+",","the segment starting at",currentPhone[startTime],\
						"sec overlaps with the segment starting at",nextPhone[startTime],"sec by more than 50 ms.",\
						"You might have to decrease the amount of padding and/or manually decrease the segment length to solve this conflict.")
				else:
					nextPhone[startTime] = currentPhone[endTime]
					print("Warning: in file",TextGrid+",","the segment starting at",nextPhone[startTime],"sec was shifted forward to resolve a",\
						"timing conflict (two overlapping segment). Please, verify manually that the shifted window still captures the segment.")
		else:
			if currentPhone[endTime] - currentPhone[startTime] < 0.025:  # each phone window must be at least 25 ms in length
				currentPhone[endTime] = currentPhone[startTime] + 0.025  # shift currentPhone's endTime to be 25 ms after startTime
				print("Note: the segment in file:",TextGrid,"at time:",currentPhone[startTime],\
				"was automatically elongated because it was shorter than the required 25 ms.\n")

		if interval == len(extendedEntryList)-1 and nextPhone[endTime] - nextPhone[startTime] < 0.025:  # if the last segment is too short
			nextPhone[endTime] = nextPhone[startTime] + 0.025  # shift currentPhone's endTime to be 25 ms after startTime

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

addStopTier('test1.1.TextGrid',['a','i','o'])








