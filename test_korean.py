import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_noStopsListArgument(self):  #1
		'''Test program implementation on 1 speaker with a 22.05kHz wav file and no stops list (defaults 
		to all voiceless stops). Only singleton and geminate stops are part of the default voiceless stops category, 
		but not other labels (eg: 'ph', 't0', etc.)'''
		calculateVOT("korean_tests/s22m37m1.wav", "korean_tests/s22m37m1.TextGrid")
		tg = tgio.openTextgrid("output/s22m37m1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['korean phones', 'korean words', 'korean stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 11)
		self.assertEqual(tgTokens, ['cc', 'kk', 'pp', 'tt'])
		

	def test_allVoicelessKoreanStops(self):  #2
		'''Test program implementation on 1 speaker with a 22.05kHz wav file and and all stops in korean.'''
		calculateVOT("korean_tests/s22m37m6.wav", 
			"korean_tests/s22m37m6.TextGrid", 
			['p0', 'ph', 'pp', 't0', 'th', 'tt', 'k0', 'kh', 'kk'])
		tg = tgio.openTextgrid("output/s22m37m6_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['korean phones', 'korean words', 'korean stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 91)
		self.assertEqual(tgTokens, ['k0', 'kh', 'kk', 'p0', 'ph', 'pp', 't0', 'tt'])




if __name__ == '__main__':
	unittest.main()