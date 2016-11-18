###Rio Scale 2.0 Calculator###

This is a simple collection of Python scripts to implement a new Rio Scale for categorising signals from Search for Extraterrestrial Intelligence (SETI) surveys.  The calculation of the scale is simply

R = Q * delta

Where Q describes the consequence or impact of the signal (if true), and delta describes the credibility of the signal.

If you want to try out the calculator, simply run

`python rio2calculator.py`

And answer the prompts in the command line.  This code should run in standard Python (written and tested in 2.7) has no other dependencies other than the module `rio2definitions.py`, which in turn only uses the standard `sys` module and the standard `input`/`raw_input` I/O.

The other scripts calculate the distribution of possible values for Q and delta, as well as R

This is still evolving, suggestions welcome!
