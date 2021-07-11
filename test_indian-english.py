import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_noStopsListArgument(self):  #1
		'''Test program implementation on 2 speaker with a 2-channel, 22.05kHz wav file and no stops list (defaults 
		to all voiceless stops). Only singleton and geminate stops are part of the default voiceless stops category, 
		which will cover all stop sounds found in english.'''
		calculateVOT(
			"indian-english_tests/DP_IN_01_IN_02_EN_IN_01_DP_IN_01_IN_02_EN_IN_02.wav", 
			"indian-english_tests/DP_IN_01_IN_02_EN_IN_01_DP_IN_01_IN_02_EN_IN_02.TextGrid", 
			distinctChannels=True
			)
		tg = tgio.openTextgrid("output/DP_IN_01_IN_02_EN_IN_01_DP_IN_01_IN_02_EN_IN_02_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumberCh1 = len(tg.tierDict[tgTiers[-4]].entryList)
		tgTokenNumberCh2 = len(tg.tierDict[tgTiers[-3]].entryList)
		tgTokensCh1 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-4]].entryList])))
		tgTokensCh2 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-3]].entryList])))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['ind 1 - words', 'ind 1 - phones', 'word - ind 2', 
			'phone - ind 2', 'ind 1 - stops', 'stops - ind 2', 'ind 1 - AutoVOT', 'AutoVOT - ind 2'])
		self.assertEqual(tgTokenNumberCh1, 57)
		self.assertEqual(tgTokensCh1, ['K', 'P', 'T'])
		self.assertEqual(tgTokenNumberCh2, 31)
		self.assertEqual(tgTokensCh2, ['K', 'P', 'T'])
		





if __name__ == '__main__':
	unittest.main()




