import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_noStopsListArgument(self):  #1
		'''Test program implementation on 1 speaker with a 22.05kHz wav file and no stops list (defaults 
		to all voiceless stops). Only singleton and geminate stops are part of the default voiceless stops category, 
		but not other labels (eg: 'ph', 't0', etc.)'''
		calculateVOT("cantonese_tests/VM34A_Cantonese_I1_20191028.wav", 
			"cantonese_tests/VM34A_Cantonese_I1_20191028.TextGrid")
		tg = tgio.openTextgrid("output/VM34A_Cantonese_I1_20191028_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 6)
		self.assertEqual(tgTiers, ['task', 'utterance', 'word', 'phone', 'stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 64)
		self.assertEqual(tgTokens, ['c', 'k', 'p', 't'])
		

	def test_allVoicelessCantoneseStops(self):  #2
		'''Test program implementation on 1 speaker with a 22.05kHz wav file and and all stops in korean.'''
		calculateVOT("cantonese_tests/VM25B_Cantonese_I2_20200224.wav", 
			"cantonese_tests/VM25B_Cantonese_I2_20200224.TextGrid", 
			['p', 't', 'k', 'kw', 'c'])
		tg = tgio.openTextgrid("output/VM25B_Cantonese_I2_20200224_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 6)
		self.assertEqual(tgTiers, ['task', 'utterance', 'word', 'phone', 'stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 48)
		self.assertEqual(tgTokens, ['c', 'k', 'p', 't'])




if __name__ == '__main__':
	unittest.main()