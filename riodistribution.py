# Written 18/11/2016 by dh4gan
# This script runs both the Q and delta questions repeatedly
# to explore all possible answers, and then compute the resulting R distribution


import rio2definitions as d
import matplotlib.pyplot as plt
import numpy as np

title = '\t\t\t RIO SCALE 2.0 Distribution \n\t\t\t -------------------------'

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


print 'Computing all possible values of delta'
print '-------------------------'

deltavalues = []

sourceanswers = indepanswers = natureanswers = instrumentanswers = repeatanswers = hoaxanswers = ["y","n"]


for source in sourceanswers:
    for indep in indepanswers:
        for nat in natureanswers:
            for inst in instrumentanswers:
                for rep in repeatanswers:
                    for hoax in hoaxanswers:

                        delta=d.ask_all_delta_questions(sourceanswer=source,indepanswer=indep,naturalanswer=nat,instrumentanswer=inst,repeatanswer=rep,hoaxanswer=hoax)
                        deltavalues.append(delta)
                



print "Computing all possible Rio values"

Riovalues = []

for Q in Qvalues:
    for delta in deltavalues:
        Rio = Q*delta
        Riovalues.append(Rio)

mean = np.mean(np.array(Riovalues))
median = np.median(np.array(Riovalues))
stdev = np.std(np.array(Riovalues))

print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(Riovalues, normed=True,bins=20)
ax1.set_xlabel("$R$", fontsize=22)
ax1.set_ylabel("Relative Frequency",fontsize=22)
plt.show()


