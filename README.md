# Rio Scale 2.0 Calculator

This repository hosts a website for calculating the Rio Scale 2.0, for categorising signals from Search for Extraterrestrial Intelligence (SETI) surveys.  The calculation of the scale is simply

*R = Q * &#948*

Where *Q* measures the consequences of the signal (if true), and *&#948* describes the probability that the signal is indeed due to extraterrestrial intelligence.


## Website 

The browser-based quiz (which runs on Javascript) can be accessed here:

<https://dh4gan.github.io/rioscale2>

The website has been tested on Chrome, Firefox and Safari (no promises about Internet Explorer).

## Python scripts

This repository also includes the quiz in Python format.  These scripts are principally used to compute statistics of the quiz, but can also be used

### Installation and use

If you want to try out the Python calculator, you will need to have Python installed locally.  Once you have that, simply pull or download the code, and run

`python rio2calculator.py`

in the code directory.  The code executes a questionnaire: answer the prompts in the command line to calculate the score.  The other script `riodistribution.py` runs the calculator through all its possible answer sets, and computes the distribution of possible values for *Q* and *&#948*, as well as *R*.

## Dependencies

`rio2calculator.py` runs in pure Python (written and tested in 2.7), and has no other module dependencies (apart from the included module `rio2definitions.py`).

`riodistribution.py` depends on numpy and matplotlib


