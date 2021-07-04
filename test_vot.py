import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_oneSpeakerVoiceless(self):  #1
		'''Test program implementation on 1 speaker with a 16kHz wav file and one voiceless stop.'''
		calculateVOT("test.wav", "testing/test1-1.TextGrid",["p"])
		tg = tgio.openTextgrid("output/test1-1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 6)
		self.assertEqual(tgTokens, ['p'])

	def test_oneSpeakerVoiced(self):  #2
		'''Test program implementation on 1 speaker with a 16kHz wav file and one voiced stop.'''
		calculateVOT("test.wav", "testing/test1-2.TextGrid",["g"])
		tg = tgio.openTextgrid("output/test1-2_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 1)
		self.assertEqual(tgTokens, ['g'])

	def test_oneSpeakerNone(self):  #3
		'''Test program implementation on 1 speaker with a 16kHz wav file and no stop tokens.'''
		calculateVOT("test.wav", "testing/test1-3.TextGrid")
		tg = tgio.openTextgrid("output/test1-3_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 21)
		self.assertEqual(tgTokens, ['k','p'])

	def test_oneSpeakerBoth(self):  #4
		'''Test program implementation on 1 speaker with a 16kHz wav file and voiceless and voiced stops.'''
		calculateVOT("test.wav", "testing/test1-4.TextGrid",['p','g'])
		tg = tgio.openTextgrid("output/test1-4_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 7)
		self.assertEqual(tgTokens, ['g','p'])

	def test_oneSpeakerShort(self):  #5
		'''Test program implementation on 1 speaker with one token shorter than 25ms.'''
		calculateVOT("test.wav", "testing/test1-5.TextGrid",["b"])
		tg = tgio.openTextgrid("output/test1-5_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 9)
		self.assertEqual(tgTokens, ['b'])

	def test_twoSpeakerVoiceless(self):  #6
		'''Test program implementation on 2 speakers with a 16kHz wav file and one voiceless stop.'''
		calculateVOT("test.wav", "testing/test2-1.TextGrid",["p"])
		tg = tgio.openTextgrid("output/test2-1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 6)
		self.assertEqual(tgTokens, ['p'])

	def test_twoSpeakerVoiced(self):  #7
		'''Test program implementation on 2 speakers with a 16kHz wav file and one voiced stop.'''
		calculateVOT("test.wav", "testing/test2-2.TextGrid",["g"])
		tg = tgio.openTextgrid("output/test2-2_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 1)
		self.assertEqual(tgTokens, ['g'])

	def test_twoSpeakerNone(self):  #8
		'''Test program implementation on 2 speakers with a 16kHz wav file and no stop tokens.'''
		calculateVOT("test.wav", "testing/test2-3.TextGrid")
		tg = tgio.openTextgrid("output/test2-3_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList])))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 21)
		self.assertEqual(tgTokens, ['k','p'])

	def test_twoSpeakerBoth(self):  #9
		'''Test program implementation on 2 speakers with a 16kHz wav file and voiceless and voiced stops.'''
		calculateVOT("test.wav", "testing/test2-4.TextGrid",['p','g'])
		tg = tgio.openTextgrid("output/test2-4_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList])))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 7)
		self.assertEqual(tgTokens, ['g','p'])

	def test_threeSpeakerVoiceless(self):  #10
		'''Test program implementation on 3 speakers with a 16kHz wav file and one voiceless stop.'''
		calculateVOT("test.wav", "testing/test3-1.TextGrid",["p"])
		tg = tgio.openTextgrid("output/test3-1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
		self.assertEqual(tgTierNumber, 12)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
			'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 6)
		self.assertEqual(tgTokens, ['p'])

	def test_threeSpeakerVoiced(self):  #11
		'''Test program implementation on 3 speakers with a 16kHz wav file and one voiced stop.'''
		calculateVOT("test.wav", "testing/test3-2.TextGrid",["g"])
		tg = tgio.openTextgrid("output/test3-2_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
		self.assertEqual(tgTierNumber, 12)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
			'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 1)
		self.assertEqual(tgTokens, ['g'])

	def test_threeSpeakerNone(self):  #12
		'''Test program implementation on 3 speakers with a 16kHz wav file and no stop tokens.'''
		calculateVOT("test.wav", "testing/test3-3.TextGrid")
		tg = tgio.openTextgrid("output/test3-3_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList])))
		self.assertEqual(tgTierNumber, 12)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
			'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 21)
		self.assertEqual(tgTokens, ['k','p'])

	def test_threeSpeakerBoth(self):  #13
		'''Test program implementation on 3 speakers with a 16kHz wav file and voiceless and voiced stops.'''
		calculateVOT("test.wav", "testing/test3-4.TextGrid",['p','g'])
		tg = tgio.openTextgrid("output/test3-4_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList])))
		self.assertEqual(tgTierNumber, 12)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
			'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 7)
		self.assertEqual(tgTokens, ['g','p'])

	def test_twoSpeakerDistinctVoiceless(self):  #14
		'''Test program implementation on 2 speakers with a 16kHz wav file and two voiceless stops.'''
		calculateVOT("test.wav", "testing/test4.TextGrid",["p","t"])
		tg = tgio.openTextgrid("output/test4_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumberP = len(tg.tierDict[tgTiers[-4]].entryList)
		tgTokenNumberT = len(tg.tierDict[tgTiers[-3]].entryList)
		tgTokensP = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
		tgTokensT = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
		self.assertEqual(tgTokenNumberP, 6)
		self.assertEqual(tgTokenNumberT, 5)
		self.assertEqual(tgTokensP, ['p'])
		self.assertEqual(tgTokensT, ['t'])

	def test_twoSpeakerDistinctVoiced(self):  #15
		'''Test program implementation on 2 speakers with a 16kHz wav file and two voiced stops.'''
		calculateVOT("test.wav", "testing/test5.TextGrid",["b","d"])
		tg = tgio.openTextgrid("output/test5_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumberD = len(tg.tierDict[tgTiers[-4]].entryList)
		tgTokenNumberB = len(tg.tierDict[tgTiers[-3]].entryList)
		tgTokensD = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
		tgTokensB = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
		self.assertEqual(tgTokenNumberD, 13)
		self.assertEqual(tgTokenNumberB, 14)
		self.assertEqual(tgTokensD, ['d'])
		self.assertEqual(tgTokensB, ['b'])

	def test_oneSpeakerTierRelabeling(self):  #16
		'''Test program implementation on 1 speaker with a 16kHz wav file and an preexisting AutoVOT tier.'''
		calculateVOT("test.wav", "testing/test6.TextGrid",["p"])
		tg = tgio.openTextgrid("output/test6_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['utt - words','utt - phones',
			'autovot - original','utt - stops','AutoVOT'])
		self.assertEqual(tgTokenNumber, 6)
		self.assertEqual(tgTokens, ['p'])

	def test_oneSpeakerNoVoiceless(self):  #17
		'''Test program implementation on 1 speaker with a 16kHz wav file and no voiceless stops.
		The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit): # check that the program stops
			calculateVOT("test.wav", "testing/test7.TextGrid")
		path = ("output/test7_output.TextGrid") # check that a file was not created
		self.assertIs(os.path.exists(path),False)

	def test_twoSpeakerNoVoiceless(self):  #18
		'''Test program implementation on 2 speakers with a 16kHz wav file and no voiceless stops.
		The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit): # check that the program stops
			calculateVOT("test.wav", "testing/test8.TextGrid")
		path = ("output/test8_output.TextGrid") # check that a file was not created
		self.assertIs(os.path.exists(path),False)

	def test_oneSpeakerExtraPadding(self):  #19
		'''Test program implementation on 1 speaker with a 16kHz wav file and excessive padding.
		The program should print a warning message indicating readjustment to 25ms.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test9-1.TextGrid",['p'],endPadding=0.03)
		self.assertEqual(len(captured.records), 3)
		self.assertEqual(captured.records[1].getMessage(), "An endPadding of 0.03 sec exceeds the maximum. "\
			"It was adjusted to 0.025 sec.\n")

	def test_oneSpeakerProximity(self):  #20
		'''Test program implementation on 1 speaker with a 16kHz wav file, maximum padding (25ms), 
		and two phones close together. The program should print a warning message indicating a 
		shift and the time in the recording where it occurred.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test9-2.TextGrid",['k'],endPadding=0.025)
		self.assertEqual(len(captured.records), 3)
		self.assertEqual(captured.records[1].getMessage(), "In File test9-2.TextGrid, the phone "\
			"starting at 23.201 was shifted forward due to a proximity issue.\n")

	def test_oneSpeakerOverlapping(self):  #21
		'''Test program implementation on 1 speaker with a 16kHz wav file and two overlapping tokens.
		The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit) as cm: # check that the program stops
			calculateVOT("test.wav", "testing/test9-3.TextGrid",['k'],endPadding=0.025)

	def test_twoSpeakerFirstProximity(self):  #22
		'''Test program implementation on 2 speakers with a 16kHz wav file and two tokens close together
		for the first speaker. The program should print a warning messages indicating the shifts 
		and the time  in the recording where they occurred.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test10.TextGrid",['k'])
		self.assertEqual(len(captured.records), 3)
		self.assertEqual(captured.records[1].getMessage(), "In File test10.TextGrid, the phone "\
			"starting at 23.201 was shifted forward due to a proximity issue.\n")

	def test_twoSpeakersFirstOverlapping(self):  #23
		'''Test program implementation on 2 speakers with a 16kHz wav file and two overlapping tokens
		for the first speaker. The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit) as cm: # check that the program stops
			calculateVOT("test.wav", "testing/test10.TextGrid",['k'],endPadding=0.025)

	def test_twoSpeakerSecondProximity(self):  #24
		'''Test program implementation on 2 speakers with a 16kHz wav file and two tokens close together
		for the second speaker. The program should print a warning messages indicating the shifts 
		and the time  in the recording where they occurred.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test11.TextGrid",['k'])
		self.assertEqual(len(captured.records), 3)
		self.assertEqual(captured.records[1].getMessage(), "In File test11.TextGrid, the phone "\
			"starting at 23.201 was shifted forward due to a proximity issue.\n")

	def test_oneSpeakerSecondOverlapping(self):  #25
		'''Test program implementation on 2 speakers with a 16kHz wav file and two overlapping tokens for
		the second speaker. The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit) as cm: # check that the program stops
			calculateVOT("test.wav", "testing/test11.TextGrid",['k'],endPadding=0.025)

	def test_inconsistentCapitalization(self):  #26
		'''Test program implementation on 2 speakers with a 16kHz wav file and two pairs of inconsistently 
		capitalized tiers. The program should conver all labels to lowercase and continue the process.'''
		calculateVOT("test.wav", "testing/test12.TextGrid",["p"])
		tg = tgio.openTextgrid("output/test12_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
			'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
		self.assertEqual(tgTokenNumber, 6)
		self.assertEqual(tgTokens, ['p'])

	def test_mismatchedTiers(self):  #27
		'''Test program implementation on 2 speakers with a 16kHz wav file but second speaker only has
		one word tier (mismatched tier pairs). The program should raise a SystemExit error and
		terminate the process.'''
		with self.assertRaises(SystemExit) as cm:
			calculateVOT("test.wav", "testing/test13.TextGrid")

	def test_noPhoneTier(self):  #28
		'''Test program implementation on 2 speakers with a 16kHz wav file but both speakers only have
		one word tier each (no phone tiers). The program should raise a SystemExit error and
		terminate the process.'''
		with self.assertRaises(SystemExit) as cm:
			calculateVOT("test.wav", "testing/test14.TextGrid")

	def test_fileFormatError(self):  #29
		'''Test program implementation on 2 speakers with a 16kHz wav file and a .txt file (not a TG). 
		The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit) as cm:
			calculateVOT("test.wav", "testing/test15.txt")

	def test_stopsTierPresent(self):  #30
		'''Test program implementation on 1 speaker with a 16kHz wav file and a preexisting 'stops' tier.
		The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit) as cm:
			calculateVOT("test.wav", "testing/test16.TextGrid")

	def test_wavTwoChannels(self):  #31
		'''Test program implementation on 1 speaker with a 16kHz wav file with two channels. The program
		should extract one channel and continue.'''
		calculateVOT("test-2ch.wav", "testing/test17.TextGrid",["p"])
		tg = tgio.openTextgrid("output/test1-1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 6)
		self.assertEqual(tgTokens, ['p'])

	def test_wavHigherSamplingRate(self):  #32
		'''Test program implementation on 1 speaker with a 22.05kHz sampling rate wav file.'''
		calculateVOT("test-22khz.wav", "testing/test18.TextGrid",["p"])
		tg = tgio.openTextgrid("output/test1-1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 6)
		self.assertEqual(tgTokens, ['p'])

	def test_oneNonStop(self):  #33
		'''Test program implementation on 1 speaker where one element in the stops list is not a stop.
		The program should remove the element from the list and continue.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test19.TextGrid",['p','a'])
		self.assertEqual(len(captured.records), 3)
		self.assertEqual(captured.records[1].getMessage(), "'a' is not a stop sound. "\
			"This symbol will be ignored in file test19.TextGrid.\n")

	def test_twoNonStops(self):  #34
		'''Test program implementation on 1 speaker where one element in the stops list is not a stop.
		The program should remove the element from the list and continue.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test20.TextGrid",['p','a','e'])
		self.assertEqual(len(captured.records), 3)
		self.assertEqual(captured.records[1].getMessage(), "'a', 'e' are not stop sounds. "\
			"These symbols will be ignored in file test20.TextGrid.\n")

	def test_onlySoundNonStop(self):  #35
		'''Test program implementation on 1 speaker where the only element in the stops list is not a stop.
		The program should remove the element from the list and continue analyzing all voiceless stops.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test21.TextGrid",['a'])
		self.assertEqual(len(captured.records), 5)
		self.assertEqual(captured.records[1].getMessage(), "'a' is not a stop sound. This symbol will "\
			"be ignored in file test21.TextGrid.\n")
		self.assertEqual(captured.records[2].getMessage(), "The sound you entered is not classified as "\
			"a stop sound by the IPA.")
		self.assertEqual(captured.records[3].getMessage(), "The program will continue by analyzing all "\
			"voiceless stops recognized by the IPA.\n")

	def test_onlyTwoSoundsNonStop(self):  #36
		'''Test program implementation on 1 speaker where the only element in the stops list is not a stop.
		The program should remove the element from the list and continue analyzing all voiceless stops.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test22.TextGrid",['a','e'])
		self.assertEqual(len(captured.records), 5)
		self.assertEqual(captured.records[1].getMessage(), "'a', 'e' are not stop sounds. These symbols "\
			"will be ignored in file test22.TextGrid.\n")
		self.assertEqual(captured.records[2].getMessage(), "Neither of the sounds you entered is classified "\
			"as a stop sound by the IPA.")
		self.assertEqual(captured.records[3].getMessage(), "The program will continue by analyzing all "\
			"voiceless stops recognized by the IPA.\n")

	def test_onlyThreeSoundsNonStop(self):  #37
		'''Test program implementation on 1 speaker where the only element in the stops list is not a stop.
		The program should remove the element from the list and continue analyzing all voiceless stops.'''
		with self.assertLogs() as captured:
			calculateVOT("test.wav", "testing/test23.TextGrid",['a','e','i'])
		self.assertEqual(len(captured.records), 5)
		self.assertEqual(captured.records[1].getMessage(), "'a', 'e', 'i' are not stop sounds. These "\
			"symbols will be ignored in file test23.TextGrid.\n")
		self.assertEqual(captured.records[2].getMessage(), "None of the sounds you entered is classified "\
			"as a stop sound by the IPA.")
		self.assertEqual(captured.records[3].getMessage(), "The program will continue by analyzing all "\
			"voiceless stops recognized by the IPA.\n")



if __name__ == '__main__':
	unittest.main()



















