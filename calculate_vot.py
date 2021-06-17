import parselmouth
import tgt

def calculateVOT(wav, TextGrid):

	# process the data
	psnd = parselmouth.Sound(wav)
	ptg = parselmouth.TextGrid.from_tgt(tgt.read_textgrid(TextGrid))

	# apply AutoVOT
	obj = parselmouth.praat.run_file([psnd,ptg],
		# "Users/ernesto/Library/Preferences/Praat\ Prefs/plugin_autovot/autovot.praat", # file on local machine # how to use this line instead of the following line?
		"autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/autovot.praat", # file on repository
		# "utt - stops", 
		# "*", 
		# "mono", 
		# 5, 
		# 500, 
		# "models/vot_predictor.amanda.max_num_instances_1000.model"
		)
	print("hello world")

	return

calculateVOT('test_audio.wav', "test1_output.TextGrid")