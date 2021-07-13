# vot-dev
Initial development of a Voice Onset Time library in Python.

___

VOT-CP (VOT coding and predictions)
=======

Ernesto R. Gutiérrez Topete (ernesto.gutierrez@berkeley.edu)\
Richard Medina (...(?))


## Description

VOT-CP is a Python program that allows for the automatic codification of phonetically aligned data in order to obtain voice onset time (VOT) predictions. This program makes use of [AutoVOT](https://github.com/mlml/autovot)'s model for generating the VOT calculations. When provided with a TextGrid that contains a word and phone tier, the program will identify all word-initial stop consonants of interest. VOT-CP will then generate and populate a new tier that can be used by AutoVOT to find the burst and onset of voicing for all selected segments. 

The program takes in:

1. `.wav` files, and
2. `.TextGrid` files with time-aligned word and phone tiers.

And it returns

1. a new TextGrid file that contains: 
  * the original word and phone tiers,
  * a tier with all the stops of interest, and 
  * a tier with VOT predictions generated by AutoVOT's model.

This program is designed to work with cross-linguistic data, and with data in various formats, for example:
  * multiple speakers in the same recording, 
  * audio files with duplicate or distinct channels, 
  * audio files with various sampling frequencies, 
  * and more.

VOT-CP does not modify the original files in any way. However, users are advised to keep a backup of all files processed with this software. Please see below for more information on the input format that is allowed or not allowed for the data processed with this program; note that some of these requirements differ from the AutoVOT program's input requirements.

This is a beta version. Any reports of bugs, suggestions for improvements to the software or the documentation, or questions are welcome and greatly appreciated.

---

### Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Tutorial](#tutorial)
4. [Citing VOT-CP](#citingvotcp)
5. [Acknowledgements](#acknowledgements)
6. [License](#license)

## Installation

### Dependencies

In order to use this program, you will need the following installed in your machine:
* [GCC, the GNU Compiler Collection](http://gcc.gnu.org/install/download.html) -- Do I need this??
* [Python (2.7 or 3)](https://www.python.org/downloads/)
* Python dependencies:
  - Run the command `pip install -r "requirements.txt"` on your terminal.
* For macOS users, complete either of the next two steps:
  - Install [Xcode](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12) -- Do I need this??
  - Download the [Command Line Tools for Xcode](http://developer.apple.com/downloads) as a stand-alone package.

### Command line installation

_VOT-CP is available from Github_.

To install the program for the first time, run the following command in your terminal window:

  ```
  $ git clone https://github.com/...
  ```

To update the VOT-CP software, navigate to the directory where the software is installed and run:

  ```
  $ git pull origin master
  ```

If you are new to Github, you can find helpful tutorials and tips for getting started here:

https://help.github.com/articles/set-up-git

## Usage

### User-provided files

VOT-CP allows for more flexibility when processing your data, for it manages certain format settings that AutoVOT does not. However, there are still certain limitations to the format of the data that can be submitted as input to the software. 

#### Audio files:

What is **allowed**:
* Can be any length (note that longer files will likely take longer to process).
* Can have one or multiple channels (see below for instructions on selecting particular channels).
* Can have any sampling frequency (provided that it is accepted by [Praat](https://www.fon.hum.uva.nl/praat/)).

What is **required**:
* Must be `.wav` files; other formats are not accepted.
* Must have a sample width of 2.
* Must not be compressed files.
* Must have stop segments in the 'phone' tier that are at least 25 ms long.
* Must have stop segments that are over 20 ms apart from each other.

#### TextGrid files:

What is **allowed**:
* Tier labels can have any capitalization, for example:
  - WORDS
  - Words
  - words
  - wOrDs
* Tier labels can have any arbitrary name (provided that the word and phone tiers match), for example:
  - 'Word', 'Phone' [both singular]
  - 'words', 'phones' [both plural]
  - 'Mary - words', 'Mary - phones' [consistent spelling and spacing]
  - 'Word-john', 'phone-John' [both singular; identifying information '-john' is placed and spelled consistently; capitalization is irrelevant]

What is **required**:
* Must be `.TextGrid` files in [full text format](https://www.fon.hum.uva.nl/praat/manual/TextGrid_file_formats.html)(ie, the default); other formats are not accepted.
* Must have a time-aligned word tier
* Must have a time-aligned phone tier
* Must have an identical inverval boundary (not close enough, identical) between word onset and start of first phone
* While the orthography (ie, alphabet) of the word tier does not matter, the label of the phone tier must use the Latin alphabet or IPA.
* Phone labels can use any romanization system (if the language does not use Latin orthography), as long as the initial element of a stop label is a stop character (ie, \<p>, \<t>, \<k>, <ʈ>, <ɟ>, etc.), for example:
  - Allowed: 't', 'p0', 'kw', 'kk', etc.
  - Not allowed: 'at', '1p', '-k', etc.

*Note that phone labels that don't use IPA or romanization will be ignored. Furthermore, any other tiers that do not contain the label 'phone(s)' or 'word(s)' (eg, 'lexical items', 'notes' or 'utterances') will also be ignored.

What is **prohibited**:
* Tier labels with inconsistent naming, for example:
  - 'Word', 'Phones' [mixture of singular and plural]
  - 'words', 'phone' [mixture of singular and plural]
  - 'Mary's - words', 'Mary - phones' [inconsistent spelling]
  - 'Mary - words', 'Mary-phones' [inconsistent spacing]
* Unequal number of word and phone tiers, for example:
  - 'Phones', 'Words-Mary', 'Phones-Mary' [an additional 'Phones' tier]
* Using the word 'stops' in any of the tier labels, for example:
  - 'stops'
  - 'stops tier'
  - 'Tier stops'
  - 'ThisIsMyStopsTier'
* Any tiers with repeated names, for example:
  - 'phones', 'words', 'phones', 'words'
* Any tiers with no name.

*Note that, to ensure precise matching of the phone and word tiers, both tiers must be identical in spelling, changing only in the words 'phone(s)' and 'word(s)'.

### Using VOT-CP

**VOT-CP can be used to process one pair of wav and TextGrid files at a time or it can be used to process an entire corpus at once. See the sections below for more information.**

#### Single wav-TextGrid pair processing

To process one pair of wav and TextGrid files at a time, use the function 
```
calculateVOT(wav, TextGrid)
```
The positinal arguments for this function are: `wav` and `TextGrid`, the two files that will be processed. See below for more information on the optional arguments.

It is recommended that new users first 

#### Batch processing

To process multiple wav and TextGrid files at once, use the function
```
calculateVOTBatch(input)
```
The sole positional argument for this function is: `input`, a string-based path which indicates the name (and location) of the directory where the wav and TextGrid files are located. If no such directory exists or if the directory name that was entered leads to an empty directory, the program will terminate immediately.

Note that this function will iterate through all items in the corpus and identify all wav and TextGrid files, ignoring any files with other extensions. Once wav and TextGrid files are identified, they will be paired with each other on the basis of their names; that is why it is important that the files match in name, for example:

  * Allowed: `S01_interview.wav` and `S01_interview.TextGrid` as well as `John.wav` and `John.TextGrid`
  * Not allowed: `S01_interview.wav` and `S1_intvw.TextGrid` nor `Mary-audio.wav` and `Mary-transcription.TextGrid`

While capitalization will be irrelevant in matching wav and TextGrid files, spelling, punctuation, and spacing will be essential.

#### Arguments

The optional arguments for single-pair processing and batch processing are: 

| Arguments          | Description |
| :---               | :---        |
| `stops`            | a list of phone labels to look for and process. For example: `['p','k']` if only bilabial and velar stops are of interest. Remember that the labels entered in this argument must match the labels in the TextGrid file, for example `['pp',"t'",'kw']` (two \<p>, a \<t> plus an apostrophe, and a \<k> plus a \<w>)). If nothing is entered for this parameter, the program will default to all voiceless singleton stops recognaized by the IPA (and their geminate form): `['p', 't', 'ʈ', 'c', 'k', 'q', 'ʔ', "p'", "t'", "k'", 'pp', 'tt', 'ʈʈ', 'cc', 'kk', 'qq', 'ʔʔ']`. |
| `outputDirectory`  | a string to be used as the name for the directory (ie, folder) were the output will be stored. If the directory already exists, the output will be stored there; otherwise, a new directory will be created with the name provided. If nothing is entered for this parameter, the program will defualt to `'output/'`. |
| `startPadding`     | a number to indicate the amount of time, *in miliseconds*, to be added to (or reduced from) the phone's start boundary. The maximam is 25 ms (or 0.025 sec), and the minimum is -25 ms (or -0.025 sec). Note that a negative value will shift the boundary left (that is, increase the segment window) and a positive value will shift the boundary right (that is, decrease the segment window). This parameter can be used when a corpus consistently marks the start boundary in its stops a little too early or a little too late. If nothing is entered for this parameter, the program will default to 0 ms (ie, no padding). |
| `endPadding`       | a number to indicate the amount of time, *in miliseconds*, to be added to (or reduced from) the phone's end boundary. The maximam is 25 ms (or 0.025 sec), and the minimum is -25 ms (or -0.025 sec). Note that a negative value will shift the boundary left (that is, decrease the segment window) and a positive value will shift the boundary right (that is, increase the segment window). This parameter can be used when a corpus consistently marks the end boundary in its stops a little too early or a little too late. If nothing is entered for this parameter, the program will default to 0 ms (ie, no padding). |
| `preferredChannel` | a number (*an integer*) that indicates the channel to be used when obtaining VOT predictions. This parameter should be used if and only if the wav file contains multiple channels, and the first channel is not the one that contains the acoustic information. If nothing is entered for this parameter, the program will default to channel 1. |
| `distinctChannels` | a boolean (ie, `True` or `False`) that indicates whether or not there are different speakers in the recording and transcription, each with a distinct channel. This occurs when two speakers are recorded simultaneously with different microphones. If nothing is entered for this parameter, the program defaults to `False`, indicating that the acoustic information for the speaker(s) in the transcription can be found in the `preferredChannel`. If the value `True` is entered for this parameter, the program will assume that there are as many channels in the wav file as there are speakers in the TextGrid file; it will then proceed to match the first pair of 'phone' and 'word' tiers to the first channel and any subsequent tier pairs to subsequent channels. |

### Additional notes

1. VOT-CP is able to process data from multiple speakers within a TextGrid (ie, multiple 'phone' and 'word' tiers in the same file), regardless of the number of channels in the wav file. In fact, if multiple phone-word tier pairs are identified in the TextGrid file, the program will automatically process all of them.

2. This program makes use of AutoVOT's latest VOT prediction model ([AutoVOT v. 0.94](https://github.com/mlml/autovot/releases/tag/0.94)). 
  * When accurately aligned data is fed to this model, it provides VOT predictions with high accuracy. If the data are not aligned accurately or if the segment windows are too big or too small, the accuracy of the predictions will decrease.
  * The current model has been trained to predict VOT for voiceless stops; in its current form, it does not support calculations of negative VOT (ie, lead voicing). 
    - Although I can say, anecdotally, that accuracy of VOT predictions for negative VOT is above chance, it is not as high as prediction accuracy for positive VOT. However, I have not investigated this issue systematically.

3. The user is advised to manually check the output data from this program. Although AutoVOT's model provides high accuracy predictions, occasional manual corrections may be required.

4. If VOT-CP does not meet your current needs based on particular transcription norms for the language(s) you study or corpus format, get in touch with me to see how the program can me re-adjusted to meet those needs.

## Tutorial

## Citing VOT-CP

VOT-CP is a general purpose program and doesn't need to be cited, but if you feel inclined, it can be cited in this way:

...(?)

However, if you use this program to analyzed data that are presented at conferences or published, it is recommended that you [cite the AutoVOT program](https://github.com/mlml/autovot/blob/master/README.md#citing).

## Acknowledgements

This software was developed as part of a summer internship hosted by [The Language Flagship Technology Innovation Center (Tech Center)](https://thelanguageflagship.tech/). 

#### Development support

Dr. Richard Medina, from the Tech Center, was the primary reserch advisor who guided the development of this program.\
Dr. Suzanne Freynik and Dr. Aitor Arronte Alvarez, both from the Tech Center, also provided support during the development phase.

#### Programming support

I want to acknowledge Yannick Jadoul, Dr. Thea Knowles, and Dr. Joseph Keshet who answered questions regarding their own programs ([Parselmouth](https://parselmouth.readthedocs.io/en/stable/) and AutoVOT).\
Yannick Jadoul also provided invaluable support in other aspects that aided in the development of the VOT-CP program.

#### Cross-linguistic corpora

Finally, I want to thank all the researchers (listed below in alphabetical order of the language), who have made their own corpora available to the public or shared them with me to allow me to test VOT-CP with cross-linguistic data.

* Arabic: 
* Cantonese: 
* (American) English: 
* (Indian) English: 
* Korean: 
* Russian: 
* Spanish: 

| test | sldfa |
| ---  | ---   |
| word | other\ word |

## License

*add license*
