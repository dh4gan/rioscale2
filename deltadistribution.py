# Written 18/11/2016 by dh4gan
# This script runs the Q questions repeatedly
# to explore all possible answers, and then compute the resulting Q distribution


import rio2definitions as d
import matplotlib.pyplot as plt
import numpy as np

title = '\t\t\t RIO SCALE 2.0 delta Distribution \n\t\t\t -------------------------'

print title


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
                                        


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)


#ax1.hist(deltavalues, normed=False, bins=np.logspace(-9, 0.0, 25))
ax1.hist(deltavalues, normed=False, log=True,log=True, bins=np.logspace(-5, 0.0, 100))
ax1.set_xscale('log')
ax1.set_xlabel("$\delta$", fontsize=22)
ax1.set_ylabel("Relative Frequency",fontsize=22)
plt.show()


