# https://billdthompson.github.io/assets/output/Jadoul2018.pdf
import parselmouth
import subprocess
import os

def calculateVOT(wav, TextGrid):

	# process the data
	# psnd = parselmouth.Sound(wav)
	# ptg = parselmouth.read(TextGrid)

	#resample audio files at 16khz
	#check for number of channels and extract first if multiple
	#

	## Terminal code
	#python 
	# autovot_shortcut/auto_vot_decode.py 
	# --vot_tier utt\ -\ stops  #check if I need to remove spaces from tiern name
	# --vot_mark k 
	# test_16.wav 
	# test1_output.TextGrid 
	# autovot_shortcut/models/vot_predictor.amanda.max_num_instances_1000.model
	
	# run the process as a child process
	# subprocess.run(['python', 'autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/auto_vot_decode.py', '-h'])
	subprocess.run([
		'python', 
		'autovot_shortcut/auto_vot_decode.py', 
		'--vot_tier', 'AutoVOT', # so these are two different arguments?
		'--vot_mark', 'k', 
		'test_16.wav', 
		'test1_output.TextGrid', 
		'autovot_shortcut/models/vot_predictor.amanda.max_num_instances_1000.model'
		])
	#error when reading the textgrid; have contact AutoVOT dev's to figure out what's going on.
	print("hello world")  #prints


	# praat plugin
	# parselmouth.praat.run_file([psnd,ptg],
	# 	"autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/autovot_form.praat", # file on repository
	# 	"utt - stops", 
	# 	"*", 
	# 	"mono", 
	# 	5, 
	# 	500, 
	# 	"models/vot_predictor.amanda.max_num_instances_1000.model"
	# 	)
	# print("hello world")  #doen't print
		# parselmouth.PraatError: System command failed.

	return

calculateVOT('test.wav', "test1_output.TextGrid")















# def fileCheck(wav, TextGrid):

# 	wavName, wavExt = os.path.splitext(wav)
# 	textgridName, textgridExt = os.path.splitext(TextGrid)

# 	if wavExt != '.wav' and textgridExt != '.TextGrid':
# 		print("The files",wav,"and",TextGrid,"do not meet format requirements;",\
# 			wav,"must be a wav file, and",TextGrid,"must be a TextGrid file.\n")
# 		return False

# 	else:
# 		print("All is good with the format of files",wav,"and",TextGrid+".\n")
# 		return True
		#sys.exit() 0=no issue, 1=exit with error



	# verify file format
	# if not fileCheck(wav, TextGrid):
	# 	return