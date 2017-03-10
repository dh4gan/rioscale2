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

                Q,info_content=d.ask_all_Q_questions(natureanswer=nat,directanswer=direct,contentanswer=content,distanceanswer=distance)

                Qvalues.append(Q)

print 'Computing all possible values of delta'
print '-------------------------'

deltavalues = []

sourceanswers = indepanswers = repeatanswers = hoaxanswers = analyseanswers=expertanswers=predictanswers=["y","n"]
info_content = [True,False]
instrumentanswers = natureanswers = [1,2,3,4]

for source in sourceanswers:
    for analyse in analyseanswers:
        for indep in indepanswers:
            for rep in repeatanswers:
                for inst in instrumentanswers:
                    for nat in natureanswers:
                        for hoax in hoaxanswers:
                            for expert in expertanswers:
                                for pred in predictanswers:
                                    for content in info_content:

                                        delta=d.ask_all_delta_questions(content, sourceanswer=source,analyseanswer=analyse,indepanswer=indep,repeatanswer=rep,instrumentanswer=inst,naturalanswer=nat,hoaxanswer=hoax, expertanswer=expert,predictanswer=pred)
                                        deltavalues.append(delta)
                                        
                      
print '-------------------------'                  
print "Computing all possible Rio values"

Riovalues = []

for Q in Qvalues:
    for delta in deltavalues:
        Rio = Q*delta
        Riovalues.append(Rio)

mean = np.mean(np.array(Qvalues))
median = np.median(np.array(Qvalues))
stdev = np.std(np.array(Qvalues))

print '-------------------------'
print "Q Statistics:"
print "Maximum: ",np.amax(Qvalues)
print "Minimum: ", np.amin(Qvalues)
print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(Qvalues, range=[1,10],normed=False,bins=10)
ax1.set_xlabel("$Q$", fontsize=22)
ax1.set_xlim(0,11)
ax1.set_ylabel("Absolute Frequency",fontsize=22)


mean = np.mean(np.array(deltavalues))
median = np.median(np.array(deltavalues))
stdev = np.std(np.array(deltavalues))
print '-------------------------'
print "Delta Statistics:"
print "Maximum: ",np.amax(deltavalues)
print "Minimum: ", np.amin(deltavalues)
print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.hist(deltavalues, range=[0,1], normed=False, log=True, bins=10)
ax2.set_xlabel("$\delta$", fontsize=22)
ax2.set_ylabel("Absolute Frequency",fontsize=22)


mean = np.mean(np.array(Riovalues))
median = np.median(np.array(Riovalues))
stdev = np.std(np.array(Riovalues))
print '-------------------------'
print "R Statistics:"
print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(Riovalues, range=[0,10], normed=False,log=True,bins=10)
ax1.set_xlabel("$R$", fontsize=22)
ax1.set_ylabel("Absolute Frequency",fontsize=22)

plt.show()



