import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	# def test_arabicOne(self):  #1
	# 	'''Test program implementation on 1 speaker with a 48kHz wav file and all voiceless coronals.'''
	# 	calculateVOT("arabic_tests/ARA_NORM__0002.wav", "arabic_tests/ARA_NORM__0002.TextGrid",["t","T","tt"],startPadding=0.25)
	# 	tg = tgio.openTextgrid("output/ARA_NORM__0002_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 5)
	# 	self.assertEqual(tgTiers, ['phones', 'words', '(11)', 'stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 3)
	# 	self.assertEqual(tgTokens, ['t']) #'tt'??

	def test_arabicTwo(self):  #2
		'''Test program implementation on 1 speaker with a 48kHz wav file and no voiceless stops.'''
		with self.assertRaises(SystemExit) as cm:
			calculateVOT("arabic_tests/ARA_NORM__0003.wav", "arabic_tests/ARA_NORM__0003.TextGrid")

	# def test_arabicThree(self):  #3
	# 	'''Test program implementation on 1 speaker with a 48kHz wav file and all voiceless coronals.'''
	# 	calculateVOT("arabic_tests/ARA_NORM__0004.wav", "arabic_tests/ARA_NORM__0004.TextGrid",["t","T","tt"])
	# 	tg = tgio.openTextgrid("output/ARA_NORM__0004_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 5)
	# 	self.assertEqual(tgTiers, ['phones', 'words', '(9)', 'stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 3)
	# 	self.assertEqual(tgTokens, ['t','tt'])



if __name__ == '__main__':
	unittest.main()