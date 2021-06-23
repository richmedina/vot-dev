# https://billdthompson.github.io/assets/output/Jadoul2018.pdf
import parselmouth
import subprocess
import os

def calculateVOT(wav, TextGrid):

	# verify file format
	if not fileCheck(wav, TextGrid):
		return

	# process the data
	psnd = parselmouth.Sound(wav)
	psndName = wav.split(".wav")[0]
	print(psndName)
	if psnd.get_sampling_frequency() != 16000:
		psnd.resample(16000).save(wav, "WAV")
	psnd = parselmouth.Sound(wav)
	if psnd.get_number_of_channels() != 1:
		psnd.extract_channel(1).save(wav, "WAV")

	# ptg = parselmouth.read(TextGrid)
	
	# run VOT predictor
	# subprocess.run(['python', 'autovot-0.94/autovot/praat_plugin/AutoVOT_Praat_plugin_v0.94/plugin_autovot/auto_vot_decode.py', '-h'])
	subprocess.run([
		'python', 
		'autovot_shortcut/auto_vot_decode.py', 
		'--vot_tier', 'utt - stops', # so these are two different arguments?
		'--vot_mark', '*', 
		wav, 
		TextGrid, 
		'autovot_shortcut/models/vot_predictor.amanda.max_num_instances_1000.model'
		])
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


def fileCheck(wav, TextGrid):

	wavName, wavExt = os.path.splitext(wav)
	textgridName, textgridExt = os.path.splitext(TextGrid)

	if wavExt != '.wav' and textgridExt != '.TextGrid':
		sys.exit(wav,"must be a wav file and",TextGrid,"must be a TextGrid file. One or both files do not meet format requirements.")

	else:
		print("All is good with the format of files",wav,"and",TextGrid+".\n")
		return True


calculateVOT('test-temp.wav', "test1_output.TextGrid")
