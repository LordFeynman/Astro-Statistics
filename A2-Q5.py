"""Astro-statistics - Assignment 2: Question 5
   @author: ronaldo"""

import numpy as np
import matplotlib.pyplot as plt

n = 10000
n_dice2 = 2
n_dice3 = 3
n_dice4 = 4
n_dice10 = 10
n_dice20 = 20

out2 = []
out3 = []
out4 = []
out10 = []
out20 = []

def roll_dice2(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll2 = np.random.randint(1,7,n_dice2)
        for i in range(n_dice2):
            score2 = sum(roll2) # Sum the values to get the score
            out2.append(score2)
        start+=1  
    return out2

def roll_dice3(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll3 = np.random.randint(1,7,n_dice3)
        for i in range(n_dice3):
            score3 = sum(roll3)  # Sum the values to get the score
            out3.append(score3)
        start+=1
    return out3

def roll_dice4(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll4 = np.random.randint(1,7,n_dice4)
        for i in range(n_dice4):
            score4 = sum(roll4)  # Sum the values to get the score
            out4.append(score4)
        start+=1
    return out4

def roll_dice10(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll10 = np.random.randint(1,7,n_dice10)
        for i in range(n_dice10):
            score10 = sum(roll10)  # Sum the values to get the score
            out10.append(score10)
        start+=1
    return out10

def roll_dice20(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll20 = np.random.randint(1,7,n_dice20)
        for i in range(n_dice20):
            score20 = sum(roll20)
            out20.append(score20)
        start += 1
    return out20

max_value2=max(roll_dice2())
max_value3=max(roll_dice3())
max_value4=max(roll_dice4())
max_value10=max(roll_dice10())
max_value20=max(roll_dice20())

# We plot the histogram only for N = 2,3,4,10

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Probability Distribution for N dice throws')
axes[0,0].hist(out2, bins = np.arange(0, max_value2+2), edgecolor='black') # N = 2
axes[0, 0].set_title('Two dice')
axes[0,1].hist(out3, bins = np.arange(0, max_value3+2), edgecolor='black') # N = 3
axes[0, 1].set_title('Three dice')
axes[1,0].hist(out4, bins = np.arange(0, max_value4+2), edgecolor='black') # N = 4
axes[1, 0].set_title('Four dice')
axes[1,1].hist(out10, bins = np.arange(0, max_value10+2), edgecolor='black') # N = 10
axes[1, 1].set_title('Ten dice')

# The plot for N=20 is similar to the N=10 one, but we didn't plot it to maintain the symmetry of the final plot

for ax in axes.flat:
    ax.set(xlabel='$X$', ylabel='$P(X)$')

fig.tight_layout()
plt.show()
