import praatio
from praatio import tgio

def addStopTier(TextGrid, stops=[], startPadding=0, endPadding=0):

	# is this where i add a file check (ie check if "TextGrid is a textgrid file")? or should it be outside of this func?
	# name, ext = os.path.splitext(TextGrid) # add file check to make sure it's a TG file?
	# if ext != '.TextGrid':
	# 	print("The file must be a TextGrid")

	tg = tgio.openTextgrid(TextGrid)

	allWordTiers = [tierName for tierName in tg.tierNameList if 'word' in tierName.lower()]
	if len(allWordTiers) == 0:
		print("This TextGrid file does not contain a tier named 'Words'")
		return
	
	allPhoneTiers = [tierName for tierName in tg.tierNameList if 'phone' in tierName.lower()]
	if len(allPhoneTiers) == 0:
		print("This TextGrid file does not contain a tier named 'Phones'")
		return
	
	if len(allWordTiers) == len(allPhoneTiers):
		# allStopTiers = []
		for tier in allWordTiers:
			print(tier)
			
			if 'Word' in tier and tier.replace('Word', 'Phone') in allPhoneTiers:
				speakerName = tier.split("Word")[0]
				wordTier = tg.tierDict[tier]
				wordStartTimes = [entry[0] for entry in wordTier.entryList]
				phoneTier = tg.tierDict[tier.replace('Word','Phone')]
				tg.addTier(processStopTier(TextGrid, speakerName, phoneTier, wordStartTimes, stops, startPadding, endPadding)) # is this the best way to pass arguments?
				# allStopTiers.append(tg.addTier(processStopTier(TextGrid, speakerName, phoneTier, wordStartTimes, stops, startPadding, endPadding)))

			elif 'word' in tier and tier.replace('word', 'phone') in allPhoneTiers:
				speakerName = tier.split("Word")[0]
				wordTier = tg.tierDict[tier]
				wordStartTimes = [entry[0] for entry in wordTier.entryList]
				phoneTier = tg.tierDict[tier.replace('word','phone')]
				tg.addTier(processStopTier(TextGrid, speakerName, phoneTier, wordStartTimes, stops, startPadding, endPadding))
				# allStopTiers.append(tg.addTier(processStopTier(TextGrid, speakerName, phoneTier, wordStartTimes, stops, startPadding, endPadding)))
			
			else:
				print("The names of the 'word' and 'phone' tiers of a given speaker are inconsistent.")
				return
	else:
		print("Error: There isn't an even number of 'phone' and 'word' tiers per speaker.")
		return
	
	# print(allStopTiers)
	# for stopTier in allStopTiers:
	# 	tg.addTier(stopTier)

	fileName = TextGrid
	saveName = fileName.split(".TextGrid")[0]

	tg.save(saveName+"_output.TextGrid")
	
	return


def processStopTier(TextGrid, speakerName, phoneTier, wordStartTimes, stops=[], startPadding=0, endPadding=0): # should i provide a defualt value for arguments here too?
	if len(stops) == 0:
		stops = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʔ', "p'", "t'", "k'", 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']

	voicedStops = ['b', 'd', 'ɖ', 'ɟ', 'g', 'ɢ', 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']

	stopEntryList,voicedTokens = [],[]
	for entry in phoneTier.entryList:
		if entry[-1].lower() in stops and entry[0] in wordStartTimes:
			stopEntryList.append(entry)
			if entry[-1].lower() in voicedStops:
				voicedTokens.append(entry[-1].lower())

	if len(voicedTokens) > 0:
		print("***Warning: You're trying to get VOT calculations of the following voiced stops: ",list(set(voicedTokens)),".")
		print("Note that AutoVOT's current model only works on voiceless stops; prevoicing may result in inaccurate calculations.")

	extendedEntryList = []

	for start, stop, label in stopEntryList:
		extendedEntryList.append([start+startPadding, stop+endPadding, label])

	fileName = TextGrid

	for interval in range(len(extendedEntryList)-1):
		if extendedEntryList[interval][1]-extendedEntryList[interval][0] < 0.025:
			extendedEntryList[interval][1] == extendedEntryList[interval][0] + 0.025
			if extendedEntryList[interval+1][0] < extendedEntryList[interval][1]:
				print("Error: There are two segments in file:",fileName,"around time:",extendedEntryList[interval][1],\
					"that either overlap with each other or are too short to calculate VOT. Fix the issue before continuing")
				print("This could be an issue resulting from adding too much 'padding'.")
				return
			else:
				print("Note: the segment in file:",fileName,"at time:",extendedEntryList[interval][0],\
				"was automatically elongated because it was shorter than the required 25 ms")
		if extendedEntryList[interval+1][0] < extendedEntryList[interval][1]:
			extendedEntryList[interval+1][0] == extendedEntryList[interval][1]
			print("Note: the start time for the segment in file:",fileName,"at time:",extendedEntryList[interval+1][0],\
				"was shifted back to resolve an issue with overlapping segments.")
			print("The issue with overlapping times could be an issue resulting from adding too much 'padding'.")

	stopTier = phoneTier.new(name = "stops", entryList = extendedEntryList)
	#print(stopTier.entryList)

	return stopTier


addStopTier('test2.TextGrid', ['k'])












