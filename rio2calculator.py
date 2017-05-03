# Written 17/11/2016 by dh4gan
# This script prompts the user for answers to several questions
# relating to signals detected in a Search for Extraterrestrial Intelligence (SETI) survey

# These answers then compute the revised Rio Scale 2.0
# R = Q * delta
# Where Q describes the consequences of a signal if true, and delta describes the credibility of the signal

import rio2definitions as d
import sys

title = '\t\t\t RIO SCALE 2.0 CALCULATOR \n\t\t\t -------------------------'

print title

print '-------------------------'
print 'Assessing consequences of signal: calculating Q'
print '-------------------------'

Q=0

info_content = False
Q = d.ask_all_Q_questions()

print "final Q value is ",Q

print '-------------------------'
print 'Now assessing credibility of signal: calculating delta'
print '-------------------------'


A,B,C,J,delta = d.ask_all_delta_questions()

Rio = Q*delta

print "Scores:"
print "Q = ",Q
print "A = ",A
print "B = ",B
print "C = ",C
print "J = ",J
print "delta = ",delta
print "Rio = ",Rio


