# https://billdthompson.github.io/assets/output/Jadoul2018.pdf
from add_stop_tier import *
from praatio import tgio
import parselmouth
import subprocess
import tempfile
import os

	#unit testing

def calculateVOT(wav, TextGrid, stops=[], outputDirectory='output', startPadding=0, endPadding=0):

	# verify file format
	if not fileCheck(wav, TextGrid):
		return

	# create directory to output files
	outputPath = os.path.join(os.getcwd(),outputDirectory)
	if not os.path.exists(outputPath):
		os.mkdir(outputPath)

	# create tier annotated with tokens of interest
	stopTier, saveName = addStopTier(TextGrid, outputPath, stops, startPadding, endPadding)
	annotatedTextgrid = os.path.join(outputDirectory, saveName)

	# make temporary directory to process predictions
	with tempfile.TemporaryDirectory() as tempDirectory:

		# process the sound file
		psnd = parselmouth.Sound(wav)
		tempSound = os.path.join(tempDirectory,wav)
		if psnd.get_sampling_frequency() != 16000:
			psnd = psnd.resample(16000)
			if psnd.get_number_of_channels() != 1:
				psnd = psnd.extract_channel(1)
		else:
			if psnd.get_number_of_channels() != 1:
				psnd = psnd.extract_channel(1)
		psnd.save(tempSound, "WAV")
		
		# run VOT predictor
		subprocess.run([
			'python', 'autovot_shortcut/auto_vot_decode.py', 
			'--vot_tier', stopTier,
			'--vot_mark', '*', 
			tempSound, 
			annotatedTextgrid, 
			'autovot_shortcut/models/vot_predictor.amanda.max_num_instances_1000.model'
			])

	return


def fileCheck(wav, TextGrid):

	wavName, wavExt = os.path.splitext(wav)
	textgridName, textgridExt = os.path.splitext(TextGrid)

	if wavExt != '.wav' and textgridExt != '.TextGrid':
		sys.exit(wav,"must be a wav file and",TextGrid,"must be a TextGrid file. One or both files do not meet format requirements.")
	else:
		print("\nProcessing",wav,"and",TextGrid+"...\n")
		return True


calculateVOT('test.wav', "testing/test1.TextGrid")








