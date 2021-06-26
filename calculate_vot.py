# https://billdthompson.github.io/assets/output/Jadoul2018.pdf
from add_stop_tier import *
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
	stopTiers, saveName, multipleSpeakers = addStopTier(TextGrid, outputPath, stops, startPadding, endPadding)
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
		for tierName in stopTiers:
			subprocess.run([
				'python', 'autovot_shortcut/auto_vot_decode.py', 
				'--vot_tier', tierName,
				'--vot_mark', '*', 
				tempSound, 
				annotatedTextgrid, 
				'autovot_shortcut/models/vot_predictor.amanda.max_num_instances_1000.model',
				'--ignore_existing_tiers'
				])

	# rename repeated labels of AutoVOT prediction tiers
	if multipleSpeakers:
		with open(annotatedTextgrid, "r") as TG:
			newTG = []
			tierNumber = 0
			for line in TG:
				if "AutoVOT" in line:
					line = line.replace("AutoVOT",stopTiers[tierNumber].split("stops")[0]+"AutoVOT")
					tierNumber += 1
				newTG.append(line)
		with open(annotatedTextgrid, "w") as TG:
			TG.writelines(newTG)
	return


def fileCheck(wav, TextGrid):

	wavName, wavExt = os.path.splitext(wav)
	textgridName, textgridExt = os.path.splitext(TextGrid)

	if wavExt != '.wav' and textgridExt != '.TextGrid':
		sys.exit(wav,"must be a wav file and",TextGrid,"must be a TextGrid file.",\
			"One or both files do not meet format requirements.")
	else:
		print("\nProcessing",wav,"and",TextGrid+"...\n")
		return True


# calculateVOT('test.wav', "testing/test13.TextGrid")

#add warning that a tier with "stops" already exists -- stop program








