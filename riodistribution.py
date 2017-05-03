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

natureanswers = [1,2,3,4,5,6,7]
directanswers = ["y","n"]
contentanswers = ["y","n"]
distanceanswers = ["y","n"]
whereanswers = [1,2,3,4]


for nat in natureanswers:
    for content in contentanswers:
            for direc in directanswers:
                for dist in distanceanswers:
                    for wh in whereanswers:

                        Q =d.ask_all_Q_questions(text=False,natureanswer=nat,contentanswer=content,directanswer=direc,distanceanswer=dist, whereanswer=wh)

                        Qvalues.append(Q)

print 'Computing all possible values of delta'
print '-------------------------'

Avalues = []
Bvalues = []
Cvalues = []
Jvalues = []
deltavalues = []

certaintyanswers=personanswers=instrumentanswers=hoaxanswers=["y","n"] 
amenableanswers=buildersanswers=[0,1,2,3]
communityanswers = range(10)
print communityanswers

for cert in certaintyanswers:
    for am in amenableanswers:
        for per in personanswers:
            for inst in instrumentanswers:
                for build in buildersanswers:
                    for h in hoaxanswers:
                        for comm in communityanswers:
                            A,B,C,J,delta=d.ask_all_delta_questions(text=False,certaintyanswer=cert,amenableanswer=am,personanswer=per,instrumentanswer=inst,buildersanswer=build,hoaxanswer=h,communityanswer=comm)
                            
                            Avalues.append(A)
                            Bvalues.append(B)
                            Cvalues.append(C)
                            Jvalues.append(J)
                            deltavalues.append(delta)
                            
                            print A,B,C,J,delta
                                        
                                      
print "Computing all possible Rio values"
print '-------------------------'

Riovalues = []

for Q in Qvalues:
    for delta in deltavalues:
        Rio = Q*delta
        Riovalues.append(Rio)

mean = np.mean(np.array(Qvalues))
median = np.median(np.array(Qvalues))
stdev = np.std(np.array(Qvalues))


print "Q Statistics:"
print "Maximum: ",np.amax(Qvalues)
print "Minimum: ", np.amin(Qvalues)
print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(Qvalues, range=[1,10],normed=True,bins=10)
ax1.set_xlabel("$Q$", fontsize=22)
ax1.set_xlim(0,11)
ax1.set_ylabel("Relative Frequency",fontsize=22)
fig1.savefig('plots/Q_distribution.png')


mean = np.mean(np.array(Jvalues))
median = np.median(np.array(Jvalues))
stdev = np.std(np.array(Jvalues))


print '-------------------------'
print "J Statistics:"
print "Maximum: ",np.amax(Jvalues)
print "Minimum: ", np.amin(Jvalues)
print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev


mean = np.mean(np.array(deltavalues))
median = np.median(np.array(deltavalues))
stdev = np.std(np.array(deltavalues))

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.hist(Jvalues, range=[0,10],normed=True,log=True,bins=100)
ax2.set_xlabel("$J$", fontsize=22)
ax2.set_xlim(0,11)
ax2.set_ylabel("Relative Frequency",fontsize=22)

fig2.savefig('plots/J_distribution.png')


print '-------------------------'
print "Delta Statistics:"
print "Maximum: ",np.amax(deltavalues)
print "Minimum: ", np.amin(deltavalues)
print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.hist(deltavalues, range=[0,1], normed=True, log=True, bins=np.logspace(-5,0,100))
ax3.set_xscale('log')
ax3.set_xlabel("$\delta$", fontsize=22)
ax3.set_ylabel("Relative Frequency",fontsize=22)
fig3.savefig('plots/delta_distribution.png')

mean = np.mean(np.array(Riovalues))
median = np.median(np.array(Riovalues))
stdev = np.std(np.array(Riovalues))
print '-------------------------'
print "R Statistics:"
print "Maximum: ",np.amax(Riovalues)
print "Minimum: ", np.amin(Riovalues)
print "Mean: ",mean
print "Median: ", median
print "Stdev: ",stdev

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.hist(Riovalues, range=[0,10], normed=True,log=True,bins=np.logspace(-5,0,100))
ax4.set_xscale('log')
ax4.set_xlabel("$R$", fontsize=22)
ax4.set_ylabel("Relative Frequency",fontsize=22)


fig4.savefig('plots/R_distribution.png')
plt.show()



