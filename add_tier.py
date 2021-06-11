import praatio
from praatio import tgio

def addTier(tg, stops=[], startPadding=0, endPadding=0):
	
	if len(stops) == 0:
		stops = ['p', 'b', 't', 'd', 'k', 'g', 'ʈ', 'ɖ', 'c', 'ɟ', 'q', 'ɢ', 'ʔ']

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

	wordStartTimes = [entry[0] for entry in wordTier]

	potentialPhoneTiers = [tierName for tierName in tg.tierNameList if 'phone' in tierName.lower()]
	if len(potentialPhoneTiers) == 0:
		print("This TextGrid file does not contain a tier named 'Phones'")
		return
	elif len(potentialPhoneTiers) >= 2:
		print("This TextGrid file has multiple tiers that contain the word 'Phone'")
		return
	else:
		phoneTier = tg.tierDict[potentialPhoneTiers[0]]

	stopEntryList = [entry for entry in phoneTier.entryList if entry[-1].lower() in stops if entry[0] in wordStartTimes]

	extendedEntryList = []

	for start, stop, label in stopEntryList:
		extendedEntryList.append([start+startPadding, stop+endPadding, label])

	stopTier = phoneTier.new(name = "stops", entryList = extendedEntryList)

	tg.addTier(stopTier)        

    #tg.save(path?/tg?) #remove

	return tg


addTier('test.TextGrid',['p'])

