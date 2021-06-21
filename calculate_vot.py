# https://billdthompson.github.io/assets/output/Jadoul2018.pdf
import parselmouth
import subprocess
import importlib
import os

def calculateVOT(wav, TextGrid):

	moduleName = input('/Users/erneto/Desktop/Projects/vot-cp/vot-dev/autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/auto_vot_decode.py')
	importlib.import_module(moduleName)
	print(moduleName)  #prints
		# ValueError: Empty module name

	# process the data
	# psnd = parselmouth.Sound(wav)
	# ptg = parselmouth.read(TextGrid)

	# suggested by RM
	# subprocess.run(['python', 'autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/auto_vot_decode.py', '-h'])
	# print("hello world")  #prints
		# ImportError: cannot import name 'izip' from 'itertools' (unknown location)

	# found online: https://www.fon.hum.uva.nl/praat/manual/Scripting_6_9__Calling_from_the_command_line.html
	# subprocess.call(["/Applications/Praat.app/Contents/MacOS/Praat", 
	# 	"--run", 
	# 	"autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/autovot_form.praat",
	# 	wav,TextGrid,
	# 	"utt - stops", 
	# 	"*", 
	# 	"mono", 
	# 	5, 
	# 	500, 
	# 	"models/vot_predictor.amanda.max_num_instances_1000.model"])
	# print("hello world")  #doesn't print
		# TypeError: expected str, bytes or os.PathLike object, not int

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