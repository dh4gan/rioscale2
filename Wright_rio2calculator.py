# Written 17/11/2016 by dh4gan
# This script prompts the user for answers to several questions
# relating to signals detected in a Search for Extraterrestrial Intelligence (SETI) survey

# These answers then compute the revised Rio Scale 2.0

# R = Q * delta

# Where Q describes the consequences of a signal if true, and delta describes the credibility of the signal

import Wright_rio2definitions as d
import sys

title = '\t\t\t RIO SCALE 2.0 CALCULATOR \n\t\t\t -------------------------'

print title

print 'Assessing consequences of signal'
print '-------------------------'

Q=0

#Q = d.ask_all_Q_questions()

Q=1

print "final Q value is ",Q

print '-------------------------'
print 'Now assessing credibility of signal'
print '-------------------------'


A,B,C,J,delta = d.ask_all_delta_questions()



Rio = delta*(2 + 4.0*Q/5.0)

print "Scores:"
print "Q = ",Q
print "A = ",A
print "B = ",B
print "C = ",C
print "J = ",J
print "delta = ",delta
print "Rio = ",Rio


