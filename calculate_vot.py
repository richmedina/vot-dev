import parselmouth
from parselmouth.praat import call as pcall
from praatio import tgio

def calculateVOT(wav, TextGrid):

	psnd = parselmouth.Sound(wav)

	# tg = parselmouth.TextGrid  #this assigns the class; it does not turn it into a praat data
	tg1 = pcall(psnd, "To TextGrid", "vot", "")  #this creates an empty textgrid
	print(tg1)
	tg2 = tgio.openTextgrid(TextGrid)  #this creates a praatio.tgio.Textgrid object
	print(tg2)

	## The code below applies to functions from Praat plugins
	# parselmouth.praat.run_file([psnd,tg], 
	# 	"autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/autovot.praat", 
	# 	"stops", 
	# 	"*", 
	# 	"mono", 
	# 	5, 
	# 	500, 
	# 	"models/vot_predictor.amanda.max_num_instances_1000.model")

	## The code below only applies to Praat's native functions
	# new_tg = pcall([psnd, tg], "AutoVOT", 
	# 	"stops", 
	# 	"*", 
	# 	"mono", 
	# 	5, 
	# 	500, 
	# 	"models/vot_predictor.amanda.max_num_instances_1000.model")

	return

calculateVOT('test_audio.wav', "test1_output.TextGrid")