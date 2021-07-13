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

1. a `.wav` file
2. a `.TextGrid` with aligned word and phone tiers

And it returns

1. a new TextGrid file that contains: 
  * the original word and phone tiers,
  * a tier with all the stops of interest, and 
  * a tier with VOT predictions generated by AutoVOT's model.

VOT-CP does not modify the original files in any way. However, users are advised to keep a backup of all files processed with this software.

This program is designed to work with cross-linguistic data, and with data in various formats, for example:
  * multiple speakers in the same recording, 
  * audio files with duplicate or distinct channels, 
  * audio files with various sampling frequencies, 
  * and more.

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
* For macOS users:
  - Install [Xcode](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12) -- Do I need this??
  - Download the [Command Line Tools for Xcode](http://developer.apple.com/downloads) as a stand-alone package.

#### Command line installation

**VOT-CP is available from Github**

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

What is **flexible**:
* Can be any length (note that longer files will likely take longer to process).
* Can have one or multiple channels (see below for instructions on selecting particular channels).
* Can have any sampling frequency (provided it's accepted by Praat).

What is **required**:
* Must be `.wav` files; other formats are not accepted.
* Must have a sample width of 2.
* Must not be a compressed file.

##### TextGrids:

What is **flexible**:
* 
* 

What is **required**:
* 
* 

#### Single wav-TextGrid pair processing

#### Batch processing

### Tutorial

### Citing VOT-CP

VOT-CP is a general purpose program and doesn't need to be cited, but if you feel inclined, it can be cited in this way:

...(?)

However, if you use this program to analyzed data that are presented at conferences or published, it is recommended that you [cite the AutoVOT program](https://github.com/mlml/autovot/blob/master/README.md#citing).

### Acknowledgements

### License *add license*
