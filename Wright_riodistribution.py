# Written 18/11/2016 by dh4gan
# This script runs both the Q and delta questions repeatedly
# to explore all possible answers, and then compute the resulting R distribution


import Wright_rio2definitions as d
import matplotlib.pyplot as plt
import numpy as np
import sys

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

Avalues = []
Bvalues = []
Cvalues = []
Jvalues = []
deltavalues = []

certainanswers = multanswers = groupanswers = routineanswers = instrumentanswers = buildersanswers= hypothesisanswers=["y","n"]
fiftyanswers = astrophysicsanswers = hoaxanswers = anthroanswers = rareanswers = ["y","n"]
communityanswers=artificialanswers = messageanswers = Janswers = ["y","n"]

for hyp in hypothesisanswers:
    for certain in certainanswers:
        for mult in multanswers:
            for group in groupanswers:
                for rout in routineanswers:
                    for inst in instrumentanswers:
                        for build in buildersanswers:
                            for fifty in fiftyanswers:
                                for astro in astrophysicsanswers:
                                    for hoax in hoaxanswers:
                                        for anthro in anthroanswers:
                                            for rare in rareanswers:
                                                for comm in communityanswers:
                                                    for art in artificialanswers:
                                                        for message in messageanswers:
                                                            for Jans in Janswers:

                                                                A,B,C,J,delta = d.ask_all_delta_questions(hypothesisanswer=hyp, certainanswer=certain,multanswer=mult,groupanswer=group,routineanswer=rout,instrumentanswer=inst,buildersanswer=build, fiftyanswer=fifty, astrophysicsanswer=astro, hoaxanswer=hoax, anthroanswer=anthro,rareanswer=rare,communityanswer=comm,artificialanswer=art, messageanswer=message, Janswer=Jans)
                                                                
                                                                Avalues.append(A)
                                                                Bvalues.append(B)
                                                                Cvalues.append(C)
                                                                Jvalues.append(J)
                                                                deltavalues.append(delta)
                                                                 
                                                                #print A, B, C, J, delta
                



print "Computing all possible Rio values"

Riovalues = []

for Q in Qvalues:
    for delta in deltavalues:
        #Rio = delta*(2 + 4.0*Q/5.0)
        Rio = Q*delta
        Riovalues.append(Rio)

mean = np.mean(np.array(Riovalues))
median = np.median(np.array(Riovalues))
stdev = np.std(np.array(Riovalues))

print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

Jvalues = np.array(Jvalues)
deltavalues = np.array(deltavalues)

print "Maximum J: ", np.amax(Jvalues)
print "Minimum J: ", np.amin(Jvalues)

mean = np.mean(np.array(Jvalues))
median = np.median(np.array(Jvalues))
stdev = np.std(np.array(Jvalues))

print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev


print "Maximum delta: ", np.amax(deltavalues)
print "Minimum delta: ", np.amin(deltavalues)

mean = np.mean(np.array(deltavalues))
median = np.median(np.array(deltavalues))
stdev = np.std(np.array(deltavalues))

print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(Riovalues, normed=False, log=True,bins=np.logspace(-5, 0.0, 100))

ax1.set_xscale('log')
ax1.set_xlabel("$R$", fontsize=22)
ax1.set_ylabel("Relative Frequency",fontsize=22)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.hist(Qvalues, normed=True,bins=100)
ax2.set_xlabel("$Q$", fontsize=22)
ax2.set_ylabel("Relative Frequency",fontsize=22)

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.hist(deltavalues, normed=False, log=True, bins=np.logspace(-5, 0.0, 100))
ax3.set_xscale('log')

ax3.set_xlabel("$\delta$", fontsize=22)
ax3.set_ylabel("Relative Frequency",fontsize=22)

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.hist(Jvalues, normed=True, bins=100,log=True)
ax4.set_xlabel("$J$", fontsize=22)
ax4.set_ylabel("Relative Frequency",fontsize=22)

fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
ax5.hist(Avalues, normed=True, bins=100, label='A')
ax5.hist(Bvalues, normed=True, bins=100, label='B')
ax5.hist(Cvalues, normed=True, bins=100, label='C')
ax5.set_xlabel("$N$", fontsize=22)
ax5.set_ylabel("Relative Frequency",fontsize=22)
ax5.legend()


plt.show()


