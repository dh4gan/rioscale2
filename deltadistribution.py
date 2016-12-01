# Written 18/11/2016 by dh4gan
# This script runs the Q questions repeatedly
# to explore all possible answers, and then compute the resulting Q distribution


import rio2definitions as d
import matplotlib.pyplot as plt

title = '\t\t\t RIO SCALE 2.0 delta Distribution \n\t\t\t -------------------------'

print title

print 'Computing all possible values of delta'
print '-------------------------'

deltavalues = []


sourceanswers = indepanswers = repeatanswers = hoaxanswers = ["y","n"]
natureanswers = instrumentanswers = [1,2,3,4]
#sourceanswers =indepanswers =["y"]

for source in sourceanswers:
    for indep in indepanswers:
        for nat in natureanswers:
            for inst in instrumentanswers:
                for rep in repeatanswers:
                    for hoax in hoaxanswers:

                        delta=d.ask_all_delta_questions(sourceanswer=source,indepanswer=indep,naturalanswer=nat,instrumentanswer=inst,repeatanswer=rep,hoaxanswer=hoax)
                        deltavalues.append(delta)
                        
                       
print deltavalues

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.hist(deltavalues, normed=True, bins=20)
ax1.set_xlabel("$\delta$", fontsize=22)
ax1.set_ylabel("Relative Frequency",fontsize=22)
plt.show()


