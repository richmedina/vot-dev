import praatio
from praatio import tgio

def addTier(tg, stops=[], startPadding=0, endPadding=0):
	
	if len(stops) == 0:
		stops = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʔ', 
		"p'", "t'", "k'", 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']

	voicedStops = ['b', 'd', 'ɖ', 'ɟ', 'g', 'ɢ', 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ']

#	name, ext = os.path.splitext(tg) # add file check to make sure it's a TG file?
#	if ext != '.TextGrid':
#		print("The file must be a TextGrid") # leave outside of func

	tg = tgio.openTextgrid(tg)

	potentialWordTiers = [tierName for tierName in tg.tierNameList if 'word' in tierName.lower()]
	if len(potentialWordTiers) == 0:
		print("This TextGrid file does not contain a tier named 'Words'")
		return
	elif len(potentialWordTiers) >= 2:
		print("This TextGrid file has multiple tiers that contain the word 'Word'")
		return
	else:
		wordTier = tg.tierDict[potentialWordTiers[0]]

	wordStartTimes = [entry[0] for entry in wordTier.entryList]

	potentialPhoneTiers = [tierName for tierName in tg.tierNameList if 'phone' in tierName.lower()]
	if len(potentialPhoneTiers) == 0:
		print("This TextGrid file does not contain a tier named 'Phones'")
		return
	elif len(potentialPhoneTiers) >= 2:
		print("This TextGrid file has multiple tiers that contain the word 'Phone'")
		return
	else:
		phoneTier = tg.tierDict[potentialPhoneTiers[0]]
	
	stopEntryList,voicedTokens = [],[]
	for entry in phoneTier.entryList:
		if entry[-1].lower() in voicedStops:
			voicedTokens.append(entry[-1].lower())
		if entry[-1].lower() in stops and entry[0] in wordStartTimes:
			stopEntryList.append(entry)

	if len(voicedTokens) > 0:
		print("***Warning: You're trying to get VOT calculations of the following voiced stops: ",list(set(voicedTokens)))
		print("Note that AutoVOT's current model only works on voiceless stops; prevoicing may result in inaccurate calculations.")

	extendedEntryList = []

	for start, stop, label in stopEntryList:
		extendedEntryList.append([start+startPadding, stop+endPadding, label])

	stopTier = phoneTier.new(name = "stops", entryList = extendedEntryList)

	tg.addTier(stopTier)        

	tg.save('test_output.TextGrid')

	return


addTier('test.TextGrid',[], 0, 0.02)

