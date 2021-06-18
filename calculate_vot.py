# https://billdthompson.github.io/assets/output/Jadoul2018.pdf
import parselmouth
import os
# import tgt

def calculateVOT(wav, TextGrid):

	# verify file format
	if not fileCheck(wav, TextGrid):
		return

	# process the data
	psnd = parselmouth.Sound(wav)
	# ptg = parselmouth.TextGrid.from_tgt(tgt.read_textgrid(TextGrid))
	ptg = parselmouth.praat.call("Read from file", TextGrid)
	# print(type(ptg))
	# print(ptg)

	# apply AutoVOT
	obj = parselmouth.praat.run_file([psnd,ptg],
		# "/Users/ernesto/Library/Preferences/Praat\ Prefs/plugin_autovot/autovot.praat", 
		# file on local machine # how to use this line instead of the following line?
		# add initial slash
		# try one dot ./
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

def fileCheck(wav, TextGrid):

	wavName, wavExt = os.path.splitext(wav)
	textgridName, textgridExt = os.path.splitext(TextGrid)

	if wavExt != '.wav' and textgridExt != '.TextGrid':
		print("The files",wav,"and",TextGrid,"do not meet format requirements;",\
			wav,"must be a wav file, and",TextGrid,"must be a TextGrid file.\n")
		return False

	else:
		print("All is good with the format of files",wav,"and",TextGrid+".\n")
		return True
		#sys.exit() 0=no issue, 1=exit with error



calculateVOT('test.wav', "test_output.TextGrid")













