import parselmouth
from parselmouth.praat import call as pcall

def calculateVOT(wav, TextGrid):

	psnd = parselmouth.Sound(wav)

	tg = parselmouth.TextGrid

	new_tg = pcall([psnd, tg], "AutoVOT", 
		"stops", 
		"*", 
		"mono", 
		5, 
		500, 
		"models/vot_predictor.amanda.max_num_instances_1000.model")

	return duration

calculateVOT('test_audio.wav', "test_output.TextGrid")