import unittest
from calculate_vot import *
from praatio import tgio

class TestVOT(unittest.TestCase):

	# def test_oneSpeakerVoiceless(self):
	# 	calculateVOT("test.wav", "testing/test1.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_oneSpeakerVoiced(self):
	# 	calculateVOT("test.wav", "testing/test1.TextGrid",["g"])
	# 	tg = tgio.openTextgrid("output/test1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 1)
	# 	self.assertEqual(tgTokens, ['g'])

	# def test_oneSpeakerNone(self):
	# 	calculateVOT("test.wav", "testing/test1.TextGrid")
	# 	tg = tgio.openTextgrid("output/test1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 21)
	# 	self.assertEqual(tgTokens, ['k','p'])

	def test_oneSpeakerBoth(self):
		calculateVOT("test.wav", "testing/test1.TextGrid",['p','g'])
		tg = tgio.openTextgrid("output/test1_output.TextGrid")
		tgTierNumber = len(tg.tierNameList)
		tgTiers = tg.tierNameList
		tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
		tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
		self.assertEqual(tgTierNumber, 4)
		self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
		self.assertEqual(tgTokenNumber, 7)
		self.assertEqual(tgTokens, ['g','p'])

	## Add print statements


if __name__ == '__main__':
	unittest.main()