# vot-dev
Initial development of a Voice Onset Time library in Python.

___

VOT-CP (VOT coding and predictions)
=======

Ernesto R. Gutiérrez Topete (ernesto.gutierrez@berkeley.edu)\
Richard Medina (...(?))


### Description

VOT-CP is a Python program that allows for the automatic codification of phonetically aligned data in order to obtain VOT predictions. This program makes use of [AutoVOT](https://github.com/mlml/autovot)'s model for generating the VOT calculations. When provided with a TextGrid that contains a word and phone tier, the program will identify all word-initial stop consonants of interest. VOT-CP will then generate and populate a new tier that can be used by AutoVOT to find the burst and onset of voicing for all selected segments. 

The program takes in:

1. a `.wav` file, and
2. a `.TextGrid` with time-aligned word and phone tiers.

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

#### Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Tutorial](#tutorial)
4. [Citing VOT-CP](#citingvotcp)
5. [Acknowledgements](#acknowledgements)
6. [License](#license)

### Installation

#### Dependencies

In order to use this program, you will need the following installed in your machine:
* [GCC, the GNU Compiler Collection](http://gcc.gnu.org/install/download.html) -- Do I need this??
* [Python (2.7 or 3)](https://www.python.org/downloads/)
* Python dependencies:
  - Run the command `pip install -r "requirements.txt"` on your terminal.
* For macOS users, complete either of the next two steps:
  - Install [Xcode](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12) -- Do I need this??
  - Download the [Command Line Tools for Xcode](http://developer.apple.com/downloads) as a stand-alone package.

#### Command line installation

_VOT-CP is available from Github_.

To install the program for the first time, run the following command:

  ```
  $ git clone https://github.com/...
  ```

To update the VOT-CP software, navigate to the directory where the software is installed and run:

  ```
  $ git pull origin master
  ```

If you are new to Github, you can find helpful tutorials and tips for getting started here:

https://help.github.com/articles/set-up-git

### Usage

#### User-provided files and directories

VOT-CP allows for more flexibility when processing your data, for it manages certain format settings that AutoVOT does not. However, there are still certain limitations to the format of the data that can be submitted as input to the software. 

##### Audio files:

What is **allowed**:
* Can be any length (note that longer files will likely take longer to process).
* Can have one or multiple channels (see below for instructions on selecting particular channels).
* Can have any sampling frequency (provided that it's accepted by [Praat](https://www.fon.hum.uva.nl/praat/)).

What is **required**:
* Must be `.wav` files; other formats are not accepted.
* Must have a sample width of 2.
* Must not be compressed files.

##### TextGrids:

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
* Must have a time-aligned word tier
* Must have a time-aligned phone tier
* Must have an identical inverval boundary (not close enough, identical) between word onset and start of first phone
* While the orthography (ie: alphabet) of the word tier does not matter, the label of the phone tier must use the Latin alphabet or IPA.
* Phone labels can use any romanization system (if the language does not use Latin orthography), as long as the initial element of a stop label is a stop character (ie: \<p>, \<t>, \<k>, <ʈ>, <ɟ>, etc.), for example:
  - Allowed: 't', 'p0', 'kw', 'kk', etc.
  - Not allowed: 'at', '1p', '-k', etc.

*Note that phone labels that don't use IPA or romanization will be ignored. Furthermore, any other tiers that do not contain the label 'phone' or 'word' (eg: 'lexical items', 'notes' or 'utterances') will also be ignored.

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

#### Using VOT-CP

**VOT-CP can be used to process one pair of wav and TextGrid files at a time or it can be used to process an entire corpus at once. See the sections below for more information.**

##### Single wav-TextGrid pair processing

To process one pair of wav and TextGrid files at a time, use the function 
```
calculateVOT()
```
The positinal arguments for this function are: `wav` and `TextGrid`, the two files that will be processed.

The optional arguments are: 

| arguments         | explanation |
| :---              | :---:       |
|`stops`            | a list of phone labels to look for and process. For example: `['p','k']` if only bilabial and velar stops are of interest. Remember that the labels passed in this argument must match the labels in the TextGrid file, for example `['pp',"t'",'kw']` (two \<p>, a \<t> plus an apostrophe, and a \<k> plus a \<w>)). |
|`outputDirectory`  |    4        |
|`startPadding`     | 3           |
|`endPadding`       |2            |
|`preferredChannel` | 1           |
|`distinctChannels` |   2         |

##### Batch processing

##### Arguments

### Tutorial

### Citing VOT-CP

VOT-CP is a general purpose program and doesn't need to be cited, but if you feel inclined, it can be cited in this way:

...(?)

However, if you use this program to analyzed data that are presented at conferences or published, it is recommended that you [cite the AutoVOT program](https://github.com/mlml/autovot/blob/master/README.md#citing).

### Acknowledgements

### License *add license*
