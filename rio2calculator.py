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

print 'Assessing consequences of signal'
print '-------------------------'

Q=0


Q=d.ask_nature_question(Q)
print "Q is ",Q

Q=d.ask_direction_question(Q)
print "Q is ",Q

Q = d.ask_content_question(Q)
print "Q is ", Q

Q = d.ask_distance_question(Q)
print "Q is ",Q


print "final Q value is ",Q



print '-------------------------'
print 'Now assessing credibility of signal'
print '-------------------------'


delta = 1

delta = d.ask_source_question(delta)
print delta

delta = d.ask_indep_question(delta)
print delta

delta = d.ask_natural_question(delta)
print delta

delta = d.ask_instrument_question(delta)
print delta

delta = d.ask_hoax_question(delta)
print delta
    
    
delta = delta/10.0

Rio = Q*delta

print "Scores:"
print "Q = ",Q
print "delta = ",delta
print "Rio = ",Rio


