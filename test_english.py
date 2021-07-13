import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_noStopsListArgument(self):  #1
		'''Test program implementation on 2 speaker with a 2-channel, 22.05kHz wav file and no stops list (defaults 
		to all voiceless stops). Only singleton and geminate stops are part of the default voiceless stops category, 
		which will cover all stop sounds found in english.'''
		calculateVOT(
			"english_tests/DP_ENF_10_ENF_11_EN_ENF_10_DP_ENF_10_ENF_11_EN_ENF_11.wav", 
			"english_tests/DP_ENF_10_ENF_11_EN_ENF_10_DP_ENF_10_ENF_11_EN_ENF_11.TextGrid", 
			distinctChannels=True
			)
		tg = tgio.openTextgrid("output/DP_ENF_10_ENF_11_EN_ENF_10_DP_ENF_10_ENF_11_EN_ENF_11_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumberCh1 = len(tg.tierDict[tgTiers[-4]].entryList)
		tgTokenNumberCh2 = len(tg.tierDict[tgTiers[-3]].entryList)
		tgTokensCh1 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-4]].entryList])))
		tgTokensCh2 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-3]].entryList])))
		self.assertEqual(tgTierNumber, 8)
		self.assertEqual(tgTiers, ['words1', 'phones1', 'words2', 
			'phones2', 'stops1', 'stops2', 'AutoVOT1', 'AutoVOT2'])
		self.assertEqual(tgTokenNumberCh1, 28)
		self.assertEqual(tgTokensCh1, ['K', 'P', 'T'])
		self.assertEqual(tgTokenNumberCh2, 20)
		self.assertEqual(tgTokensCh2, ['K', 'P', 'T'])
		

	# def test_noStopsListArgument(self):  #1
	# 	'''Test program implementation on 2 speaker with a 2-channel, 22.05kHz wav file and only /p/ stops.'''
	# 	calculateVOT(
	# 		"english_tests/DP_EN_03_EN_05_EN_EN_03_DP_EN_03_EN_05_EN_EN_05.wav", 
	# 		"english_tests/DP_EN_03_EN_05_EN_EN_03_DP_EN_03_EN_05_EN_EN_05.TextGrid", 
	# 		stops = ['p'],
	# 		distinctChannels=True
	# 		)
	# 	tg = tgio.openTextgrid("output/DP_EN_03_EN_05_EN_EN_03_DP_EN_03_EN_05_EN_EN_05_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumberCh1 = len(tg.tierDict[tgTiers[-4]].entryList)
	# 	tgTokenNumberCh2 = len(tg.tierDict[tgTiers[-3]].entryList)
	# 	tgTokensCh1 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-4]].entryList])))
	# 	tgTokensCh2 = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-3]].entryList])))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['1-words', '1-phones', '2-words', 
	# 		'2-phones', '1-stops', '2-stops', '1-AutoVOT', '2-AutoVOT'])
	# 	self.assertEqual(tgTokenNumberCh1, 13)
	# 	self.assertEqual(tgTokensCh1, ['P'])
	# 	self.assertEqual(tgTokenNumberCh2, 21)
	# 	self.assertEqual(tgTokensCh2, ['P'])




if __name__ == '__main__':
	unittest.main()