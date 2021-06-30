import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	# def test_oneSpeakerVoiceless(self):  #1
	# 	calculateVOT("test.wav", "testing/test1-1.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test1-1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_oneSpeakerVoiced(self):  #2
	# 	calculateVOT("test.wav", "testing/test1-2.TextGrid",["g"])
	# 	tg = tgio.openTextgrid("output/test1-2_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 1)
	# 	self.assertEqual(tgTokens, ['g'])

	# def test_oneSpeakerNone(self):  #3
	# 	calculateVOT("test.wav", "testing/test1-3.TextGrid")
	# 	tg = tgio.openTextgrid("output/test1-3_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 21)
	# 	self.assertEqual(tgTokens, ['k','p'])

	# def test_oneSpeakerBoth(self):  #4
	# 	calculateVOT("test.wav", "testing/test1-4.TextGrid",['p','g'])
	# 	tg = tgio.openTextgrid("output/test1-4_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 7)
	# 	self.assertEqual(tgTokens, ['g','p'])

	# def test_oneSpeakerShort(self):  #5
	# 	calculateVOT("test.wav", "testing/test1-5.TextGrid",["b"])
	# 	tg = tgio.openTextgrid("output/test1-5_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 9)
	# 	self.assertEqual(tgTokens, ['b'])

	# def test_twoSpeakerVoiceless(self):  #6
	# 	calculateVOT("test.wav", "testing/test2-1.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test2-1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_twoSpeakerVoiced(self):  #7
	# 	calculateVOT("test.wav", "testing/test2-2.TextGrid",["g"])
	# 	tg = tgio.openTextgrid("output/test2-2_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 1)
	# 	self.assertEqual(tgTokens, ['g'])

	# def test_twoSpeakerNone(self):  #8
	# 	calculateVOT("test.wav", "testing/test2-3.TextGrid")
	# 	tg = tgio.openTextgrid("output/test2-3_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList])))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 21)
	# 	self.assertEqual(tgTokens, ['k','p'])

	# def test_twoSpeakerBoth(self):  #9
	# 	calculateVOT("test.wav", "testing/test2-4.TextGrid",['p','g'])
	# 	tg = tgio.openTextgrid("output/test2-4_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList])))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 7)
	# 	self.assertEqual(tgTokens, ['g','p'])

	# def test_threeSpeakerVoiceless(self):  #10
	# 	calculateVOT("test.wav", "testing/test3-1.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test3-1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_threeSpeakerVoiced(self):  #11
	# 	calculateVOT("test.wav", "testing/test3-2.TextGrid",["g"])
	# 	tg = tgio.openTextgrid("output/test3-2_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 1)
	# 	self.assertEqual(tgTokens, ['g'])

	# def test_threeSpeakerNone(self):  #12
	# 	calculateVOT("test.wav", "testing/test3-3.TextGrid")
	# 	tg = tgio.openTextgrid("output/test3-3_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList])))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 21)
	# 	self.assertEqual(tgTokens, ['k','p'])

	# def test_threeSpeakerBoth(self):  #13
	# 	calculateVOT("test.wav", "testing/test3-4.TextGrid",['p','g'])
	# 	tg = tgio.openTextgrid("output/test3-4_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList])))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 7)
	# 	self.assertEqual(tgTokens, ['g','p'])

	# def test_twoSpeakerDistinctVoiceless(self):  #14
	# 	calculateVOT("test.wav", "testing/test4.TextGrid",["p","t"])
	# 	tg = tgio.openTextgrid("output/test4_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumberP = len(tg.tierDict[tgTiers[-4]].entryList)
	# 	tgTokenNumberT = len(tg.tierDict[tgTiers[-3]].entryList)
	# 	tgTokensP = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
	# 	tgTokensT = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumberP, 6)
	# 	self.assertEqual(tgTokenNumberT, 5)
	# 	self.assertEqual(tgTokensP, ['p'])
	# 	self.assertEqual(tgTokensT, ['t'])

	# def test_twoSpeakerDistinctVoiced(self):  #15
	# 	calculateVOT("test.wav", "testing/test5.TextGrid",["b","d"])
	# 	tg = tgio.openTextgrid("output/test5_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumberD = len(tg.tierDict[tgTiers[-4]].entryList)
	# 	tgTokenNumberB = len(tg.tierDict[tgTiers[-3]].entryList)
	# 	tgTokensD = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
	# 	tgTokensB = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumberD, 13)
	# 	self.assertEqual(tgTokenNumberB, 14)
	# 	self.assertEqual(tgTokensD, ['d'])
	# 	self.assertEqual(tgTokensB, ['b'])

	# def test_oneSpeakerTierRelabeling(self):  #16
	# 	calculateVOT("test.wav", "testing/test6.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test6_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 5)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones',
	# 		'autovot - original','utt - stops','AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_oneSpeakerNoVoiceless(self):  #17
	# 	with self.assertRaises(SystemExit): # check that the program stops
	# 		calculateVOT("test.wav", "testing/test7.TextGrid")
	# 	path = ("output/test7_output.TextGrid") # check that a file was not created
	# 	self.assertIs(os.path.exists(path),False)

	# def test_twoSpeakerNoVoiceless(self):  #18
	# 	with self.assertRaises(SystemExit): # check that the program stops
	# 		calculateVOT("test.wav", "testing/test8.TextGrid")
	# 	path = ("output/test8_output.TextGrid") # check that a file was not created
	# 	self.assertIs(os.path.exists(path),False)

	# def test_oneSpeakerExtraPadding(self):  #19
	# 	with self.assertLogs() as captured:
	# 		calculateVOT("test.wav", "testing/test9-1.TextGrid",['p'],endPadding=0.03)
	# 	self.assertEqual(len(captured.records), 1)
	# 	self.assertEqual(captured.records[0].getMessage(), "An endPadding of 0.03 sec exceeds the maximum. "\
	# 		"It was adjusted to 0.025 sec.")

	# def test_oneSpeakerProximity(self):  #20
	# 	with self.assertLogs() as captured:
	# 		calculateVOT("test.wav", "testing/test9-2.TextGrid",['k'],endPadding=0.025)
	# 	self.assertEqual(len(captured.records), 1)
	# 	self.assertEqual(captured.records[0].getMessage(), "In File test9-2.TextGrid, the phone starting at 23.201 "\
	# 		"was shifted forward due to a proximity issue.")

	# def test_oneSpeakerOverlapping(self):  #21
	# 	with self.assertRaises(SystemExit) as cm: # check that the program stops
	# 		calculateVOT("test.wav", "testing/test9-3.TextGrid",['k'],endPadding=0.025)

	# def test_twoSpeakerProximity(self):  #22
	# 	with self.assertLogs() as captured:
	# 		calculateVOT("test.wav", "testing/test10.TextGrid",['k'])
	# 	self.assertEqual(len(captured.records), 1)
	# 	self.assertEqual(captured.records[0].getMessage(), "In File test10.TextGrid, the phone starting at 23.201 "\
	# 		"was shifted forward due to a proximity issue.")

	# def test_oneSpeakerOverlapping(self):  #23
	# 	with self.assertRaises(SystemExit) as cm: # check that the program stops
	# 		calculateVOT("test.wav", "testing/test10.TextGrid",['k'],endPadding=0.025)

	# def test_twoSpeakerProximity(self):  #24
	# 	with self.assertLogs() as captured:
	# 		calculateVOT("test.wav", "testing/test11.TextGrid",['k'])
	# 	self.assertEqual(len(captured.records), 1)
	# 	self.assertEqual(captured.records[0].getMessage(), "In File test11.TextGrid, the phone starting at 23.201 "\
	# 		"was shifted forward due to a proximity issue.")

	# def test_oneSpeakerOverlapping(self):  #25
	# 	with self.assertRaises(SystemExit) as cm: # check that the program stops
	# 		calculateVOT("test.wav", "testing/test11.TextGrid",['k'],endPadding=0.025)

	# def test_inconsistentCapitalization(self):  #26
	# 	calculateVOT("test.wav", "testing/test12.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test12_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_mismatchedTiers(self):  #27
	# 	with self.assertRaises(SystemExit) as cm:
	# 		calculateVOT("test.wav", "testing/test13.TextGrid")

	# def test_noPhoneTier(self):  #28
	# 	with self.assertRaises(SystemExit) as cm:
	# 		calculateVOT("test.wav", "testing/test14.TextGrid")

	# def test_fileFormatError(self):  #29
	# 	with self.assertRaises(SystemExit) as cm:
	# 		calculateVOT("test.wav", "testing/test15.txt")

	def test_stopsTierPresent(self):  #30
		with self.assertRaises(SystemExit) as cm:
			calculateVOT("test.wav", "testing/test16.TextGrid")



if __name__ == '__main__':
	unittest.main()



















