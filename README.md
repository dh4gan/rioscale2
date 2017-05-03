# Rio Scale 2.0 Calculator

This is a simple collection of Python scripts to implement a new Rio Scale for categorising signals from Search for Extraterrestrial Intelligence (SETI) surveys.  The calculation of the scale is simply

*R = Q * delta*

Where *Q* describes the consequence or impact of the signal (if true), and *delta* describes the credibility of the signal.

## Installation and use

If you want to try out the calculator, simply pull or download the code, and run

`python rio2calculator.py`

in the code directory.  The code executes a questionnaire: answer the prompts in the command line to calculate the score.  The other script `riodistribution.py` runs the calculator through all its possible answer sets, and computes the distribution of possible values for *Q* and *delta*, as well as *R*.

## Dependencies

This code runs in pure Python (written and tested in 2.7), and has no other module dependencies (apart from the included module `rio2definitions.py`).


