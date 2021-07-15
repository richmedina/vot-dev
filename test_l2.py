import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_L2ChineseKorean(self):  #1
		'''Test program implementation on 2 speaker with a 2-channel, 22.05kHz wav file and no stops list (defaults 
		to all voiceless stops). Only singleton and geminate stops are part of the default voiceless stops category, 
		which will cover all stop sounds found in english.'''
		calculateVOT(
			"l2_tests/DP_CHF_04_KOF_03_EN_KOF_03_DP_CHF_04_KOF_03_EN_CHF_04.wav", 
			"l2_tests/DP_CHF_04_KOF_03_EN_KOF_03_DP_CHF_04_KOF_03_EN_CHF_04.TextGrid", 
			distinctChannels=True
			)
		tg = tgio.openTextgrid("output/DP_CHF_04_KOF_03_EN_KOF_03_DP_CHF_04_KOF_03_EN_CHF_04_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumberCh1 = len(tg.tierDict[tgTiers[-4]].entryList)
		tgTokenNumberCh2 = len(tg.tierDict[tgTiers[-3]].entryList)
		tgTokensCh1 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-4]].entryList])))
		tgTokensCh2 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-3]].entryList])))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['words-ch', 'phones-ch', 'words-ko', 
			'phones-ko', 'stops-ch', 'stops-ko', 'AutoVOT-ch', 'AutoVOT-ko'])
		self.assertEqual(tgTokenNumberCh1, 49)
		self.assertEqual(tgTokensCh1, ['K', 'P', 'T'])
		self.assertEqual(tgTokenNumberCh2, 44)
		self.assertEqual(tgTokensCh2, ['K', 'P', 'T'])
	
	def test_L2ThaiKorean(self):  #2
		'''Test program implementation on 2 speaker with a 2-channel, 22.05kHz wav file and no stops list (defaults 
		to all voiceless stops). Only singleton and geminate stops are part of the default voiceless stops category, 
		which will cover all stop sounds found in english.'''
		calculateVOT(
			"l2_tests/DP_TH_01_KO_05_EN_TH_01_DP_TH_01_KO_05_EN_KO_05.wav", 
			"l2_tests/DP_TH_01_KO_05_EN_TH_01_DP_TH_01_KO_05_EN_KO_05.TextGrid", 
			distinctChannels=True
			)
		tg = tgio.openTextgrid("output/DP_TH_01_KO_05_EN_TH_01_DP_TH_01_KO_05_EN_KO_05_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumberCh1 = len(tg.tierDict[tgTiers[-4]].entryList)
		tgTokenNumberCh2 = len(tg.tierDict[tgTiers[-3]].entryList)
		tgTokensCh1 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-4]].entryList])))
		tgTokensCh2 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-3]].entryList])))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['words - thai', 'phones - thai', 'words - ko', 
			'phones - ko', 'stops - thai', 'stops - ko', 'AutoVOT - thai', 'AutoVOT - ko'])
		self.assertEqual(tgTokenNumberCh1, 32)
		self.assertEqual(tgTokensCh1, ['K', 'P', 'T'])
		self.assertEqual(tgTokenNumberCh2, 29)
		self.assertEqual(tgTokensCh2, ['K', 'P', 'T'])





if __name__ == '__main__':
	unittest.main()
