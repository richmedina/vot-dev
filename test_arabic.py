import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_NoVoicelessStops(self):  #1
		'''Test program implementation on 1 speaker with a 48kHz wav file and no voiceless stops.
		The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit), self.assertLogs() as captured: # check that the program stops and its logs
			calculateVOT("arabic_tests/ARA_NORM__0001.wav", "arabic_tests/ARA_NORM__0001.TextGrid")
		path = ("output/ARA_NORM__0001.TextGrid")  # map the potential path
		self.assertIs(os.path.exists(path), False)  # check that a file was not created
		self.assertEqual(len(captured.records), 2)  # check that the expected messages are logged
		self.assertEqual(captured.records[1].getMessage(), "There were no voiceless stops found in ARA_NORM__0001.TextGrid.\n")

	def test_noStopsListArgument(self):  #2
		'''Test program implementation on 1 speaker with a 48kHz wav file and no stops list (defaults to all voiceless stops).'''
		calculateVOT("arabic_tests/ARA_NORM__0002.wav", 
			"arabic_tests/ARA_NORM__0002.TextGrid")
		tg = tgio.openTextgrid("output/ARA_NORM__0002_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['phones', 'words', 'smthg', 'stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 4)
		self.assertEqual(tgTokens, ['T', 't', 'tt'])

	def test_unnamedTier(self):  #3
		'''Test program implementation on 1 speaker with an unname tier. 
		The program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit), self.assertLogs() as captured: # check that the program stops and its logs
			calculateVOT("arabic_tests/ARA_NORM__0003.wav", "arabic_tests/ARA_NORM__0003.TextGrid")
		path = ("output/ARA_NORM__0003.TextGrid")  # map the potential path
		self.assertIs(os.path.exists(path), False)  # check that a file was not created
		self.assertEqual(len(captured.records), 2)  # check that the expected messages are logged
		self.assertEqual(captured.records[1].getMessage(), "At least one tier in file arabic_tests/ARA_NORM__0003.TextGrid"\
			" has no name. Fix the issue before continuing.\n")

	def test_arabicFour(self):  #4
		'''Test program implementation on 1 speaker with a 48kHz wav file and all voiceless in arabic.'''
		calculateVOT("arabic_tests/ARA_NORM__0004.wav", "arabic_tests/ARA_NORM__0004-1.TextGrid", 
			["p","pp","t","T","tt","k","kk","q","qq"])
		tg = tgio.openTextgrid("output/ARA_NORM__0004_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['phones', 'words', 'smthg', 'stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 3)
		self.assertEqual(tgTokens, ['t','tt'])

	def test_arabicFour(self):  #4
		'''Test program implementation on 1 speaker with a 48kHz wav file and all voiceless in arabic.'''
		calculateVOT("arabic_tests/ARA_NORM__0004.wav", "arabic_tests/ARA_NORM__0004-2.TextGrid", 
			["p","t","T","k","q"])
		tg = tgio.openTextgrid("output/ARA_NORM__0004_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['phones', 'words', 'smthg', 'stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 3)
		self.assertEqual(tgTokens, ['t','tt'])

	def test_arabicFive(self):  #5
		'''Test program implementation on 1 speaker with a 48kHz wav file and all voiceless coronals.'''
		calculateVOT("arabic_tests/ARA_NORM__0005.wav", "arabic_tests/ARA_NORM__0005.TextGrid")
		tg = tgio.openTextgrid("output/ARA_NORM__0005_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['phones', 'words', 'stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 1)
		self.assertEqual(tgTokens, ['t'])

	# def test_arabicAnnotatedStops



if __name__ == '__main__':
	unittest.main()

