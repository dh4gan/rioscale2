# Written 18/11/2016 by dh4gan
# This script runs the Q questions repeatedly
# to explore all possible answers, and then compute the resulting Q distribution


import rio2definitions as d
import matplotlib.pyplot as plt
import numpy as np

title = '\t\t\t RIO SCALE 2.0 Q Distribution \n\t\t\t -------------------------'

print title

print 'Computing all possible values of Q'
print '-------------------------'

Qvalues = []

natureanswers = [1,2,3,4,5]
directanswers = ["y","n"]
contentanswers = ["y","n"]
distanceanswers = [1,2,3,4,5]


for nat in natureanswers:
    for direct in directanswers:
        for content in contentanswers:
            for distance in distanceanswers:

                Q=d.ask_all_Q_questions(natureanswer=nat,directanswer=direct,contentanswer=content,distanceanswer=distance)

                Qvalues.append(Q)
            
mean = np.mean(np.array(Qvalues))
stdev = np.std(np.array(Qvalues))

print "The mean Q is ",mean
print "stdev: ",stdev

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(Qvalues, normed=True,bins=10)
ax1.set_xlabel("$Q$", fontsize=22)
ax1.set_ylabel("Relative Frequency",fontsize=22)
plt.show()


