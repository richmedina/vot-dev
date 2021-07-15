import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	def test_noStopsListArgument(self):  #1
		'''Test program implementation on 1 speaker with a 2-channel, 22.05kHz wav file and no stops list (defaults 
		to all voiceless stops). Only singleton and geminate stops are part of the default voiceless stops category, 
		but not other labels (eg: 'p_j', 't_j', etc.)'''
		calculateVOT("russian_tests/MaSS_Russian1.wav", "russian_tests/MaSS_Russian1.TextGrid")
		tg = tgio.openTextgrid("output/MaSS_Russian1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['ort', 'russian words', 'russian phones', 'russian stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 20)
		self.assertEqual(tgTokens, ['k', 'p', 't'])
		

	def test_allVoicelessPalatalized(self):  #2
		'''Test program implementation on 1 speaker with a 2-channel, 22.05kHz wav file and all voiceless palatalized 
		stops in russian.'''
		calculateVOT("russian_tests/MaSS_Russian2.wav", "russian_tests/MaSS_Russian2-1.TextGrid", ["p_j", "t_j", "k_j"])
		tg = tgio.openTextgrid("output/MaSS_Russian2-1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['ort', 'russian words', 'russian phones', 'russian stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 4)
		self.assertEqual(tgTokens, ['p_j', 't_j'])

	def test_allVoicelessPalatalizedSecondChannel(self):  #3
		'''Test program implementation on 1 speaker with a 2-channel, 22.05kHz wav file and all voiceless palatalized 
		stops in russian. Choose the second channel to analyzed, rather than the default first channel.'''
		calculateVOT("russian_tests/MaSS_Russian2.wav", 
			"russian_tests/MaSS_Russian2-2.TextGrid", 
			["p_j", "t_j", "k_j"],
			preferredChannel=2)
		tg = tgio.openTextgrid("output/MaSS_Russian2-2_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['ort', 'russian words', 'russian phones', 'russian stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 4)
		self.assertEqual(tgTokens, ['p_j', 't_j'])

	def test_noPalatalizedVelarStops(self):  #4
		'''Test program implementation on 1 speaker with a 2-channel, 22.05kHz wav file and only palatalized velar stops 
		in russian. There are none in this file, so program should raise a SystemExit error and terminate the process.'''
		with self.assertRaises(SystemExit), self.assertLogs() as captured: # check that the program stops and its logs
			calculateVOT("russian_tests/MaSS_Russian3.wav", "russian_tests/MaSS_Russian3.TextGrid", ["k_j", "g_j"])
		path = ("output/MaSS_Russian3_output.TextGrid")  # map the potential path
		self.assertIs(os.path.exists(path), False)  # check that a file was not created
		self.assertEqual(len(captured.records), 2)  # check that the expected messages are logged
		self.assertEqual(captured.records[1].getMessage(), "There were no voiceless stops found in MaSS_Russian3.TextGrid.\n")

	def test_allVoicelessRussianStops(self):  #5
		'''Test program implementation on 1 speaker with a 2-channel, 22.05kHz wav file and all stops in russian.'''
		calculateVOT("russian_tests/MaSS_Russian4.wav", "russian_tests/MaSS_Russian4.TextGrid", 
			["p", "p_j", "t", "t_j", "k", "k_j"])
		tg = tgio.openTextgrid("output/MaSS_Russian4_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['ort', 'russian words', 'russian phones', 'russian stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 59)
		self.assertEqual(tgTokens, ['k', "p", "p_j", "t", 't_j'])

	def test_onlyPalatalizedVelarStops(self):  #6
		'''Test program implementation on 1 speaker with a 2-channel, 22.05kHz wav file and all voiceless stops in russian.'''
		calculateVOT("russian_tests/MaSS_Russian5.wav", "russian_tests/MaSS_Russian5.TextGrid", ["k_j", "g_j"])
		tg = tgio.openTextgrid("output/MaSS_Russian5_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start, end, label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 5)
		self.assertEqual(tgTiers, ['ort', 'russian words', 'russian phones', 'russian stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 3)
		self.assertEqual(tgTokens, ["g_j"])





if __name__ == '__main__':
	unittest.main()