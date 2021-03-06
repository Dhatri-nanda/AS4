# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13gbnFA1BtKpSHOJ1rRKbkplJjWhxpQg1
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from random import choices
import subprocess
import shlex

# defining random variable X where 1 represents a non_defective bulb is drawn
X=[0,1] 
#probability distribution for second draw if in first draw a black ball is drawn
pr_def=[1/9,8/9]
#probability distribution for second draw if in first draw a red ball is drawn
pr_not_def=[2/9,7/9]
#10000 simulations
simlen = 100000
#probability of drawing non_defective bulb in first draw
prob = 8/10
#generating data for first draw
data_bern = bernoulli.rvs(size=simlen,p=prob)
#generating data for second draw
b=[0]*(simlen)
for i in range(simlen):
    if (data_bern[i] == 1) :
       b[i]=random.choices(X,pr_not_def)
# counting number of 1's in data for second draw        
num_nd=b.count([1])
#calculating probability of non_defective bulb in second draw
pr_nd=num_nd/simlen
print("simulated probability is %f, which is equal to the the theoretical probability 0.622"%(pr_nd))

#plotting
cases = ["x = 1"]
prob_T = [28/45]
prob_S = [pr_nd]

x = np.arange(len(cases))
plt.stem(x + 0.00, prob_T, markerfmt='o',use_line_collection=True, basefmt=None , linefmt='orange' ,label='Theoritical')
plt.stem(x + 0.25, prob_S, markerfmt='o', use_line_collection=True, basefmt=None  ,linefmt='b', label='Simulated')
plt.xlabel('Cases')
plt.ylabel('Probability')
plt.xticks(x + 0.25/2,[1])
plt.legend()
plt.grid()
plt.show()