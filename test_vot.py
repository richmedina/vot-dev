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

	# def test_oneSpeakerBoth(self):
	# 	calculateVOT("test.wav", "testing/test1.TextGrid",['p','g'])
	# 	tg = tgio.openTextgrid("output/test1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList])))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 7)
	# 	self.assertEqual(tgTokens, ['g','p'])

	### Add print statements

	# def test_twoSpeakerVoiceless(self):
	# 	calculateVOT("test.wav", "testing/test2.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test2_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_twoSpeakerVoiced(self):
	# 	calculateVOT("test.wav", "testing/test2.TextGrid",["g"])
	# 	tg = tgio.openTextgrid("output/test2_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList]))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 1)
	# 	self.assertEqual(tgTokens, ['g'])

	# def test_twoSpeakerNone(self):
	# 	calculateVOT("test.wav", "testing/test2.TextGrid")
	# 	tg = tgio.openTextgrid("output/test2_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList])))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 21)
	# 	self.assertEqual(tgTokens, ['k','p'])

	# def test_twoSpeakerBoth(self):
	# 	calculateVOT("test.wav", "testing/test2.TextGrid",['p','g'])
	# 	tg = tgio.openTextgrid("output/test2_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-3]].entryList])))
	# 	self.assertEqual(tgTierNumber, 8)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt - stops','utt 2 - stops','utt - AutoVOT','utt 2 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 7)
	# 	self.assertEqual(tgTokens, ['g','p'])

	# def test_threeSpeakerVoiceless(self):
	# 	calculateVOT("test.wav", "testing/test3.TextGrid",["p"])
	# 	tg = tgio.openTextgrid("output/test3_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 6)
	# 	self.assertEqual(tgTokens, ['p'])

	# def test_threeSpeakerVoiced(self):
	# 	calculateVOT("test.wav", "testing/test3.TextGrid",["g"])
	# 	tg = tgio.openTextgrid("output/test3_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList]))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 1)
	# 	self.assertEqual(tgTokens, ['g'])

	# def test_threeSpeakerNone(self):
	# 	calculateVOT("test.wav", "testing/test3.TextGrid")
	# 	tg = tgio.openTextgrid("output/test3_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList])))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 21)
	# 	self.assertEqual(tgTokens, ['k','p'])

	# def test_threeSpeakerBoth(self):
	# 	calculateVOT("test.wav", "testing/test3.TextGrid",['p','g'])
	# 	tg = tgio.openTextgrid("output/test3_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-1]].entryList)
	# 	tgTokens = sorted(list(set([label for start,end,label in tg.tierDict[tgTiers[-4]].entryList])))
	# 	self.assertEqual(tgTierNumber, 12)
	# 	self.assertEqual(tgTiers, ['utt - words','utt - phones','utt 2 - words','utt 2 - phones',
	# 		'utt 3 - words','utt 3 - phones','utt - stops','utt 2 - stops','utt 3 - stops',
	# 		'utt - AutoVOT','utt 2 - AutoVOT','utt 3 - AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 7)
	# 	self.assertEqual(tgTokens, ['g','p'])

	# def test_oneSpeakerVoiced(self):
	# 	calculateVOT("test.wav", "testing/test1.TextGrid",["b"])
	# 	tg = tgio.openTextgrid("output/test1_output.TextGrid")
	# 	tgTierNumber = len(tg.tierNameList)
	# 	tgTiers = tg.tierNameList
	# 	tgTokenNumber = len(tg.tierDict[tgTiers[-2]].entryList)
	# 	tgTokens = list(set([label for start,end,label in tg.tierDict[tgTiers[-2]].entryList]))
	# 	self.assertEqual(tgTierNumber, 4)
	# 	self.assertEqual(tgTiers, ['utt - words', 'utt - phones', 'utt - stops', 'AutoVOT'])
	# 	self.assertEqual(tgTokenNumber, 9)
	# 	self.assertEqual(tgTokens, ['b'])


if __name__ == '__main__':
	unittest.main()