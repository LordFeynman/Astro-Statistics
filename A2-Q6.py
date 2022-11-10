"""Astro-statistics - Assignment 2: Question 6"""

import numpy as np
import matplotlib.pyplot as plt

# define the variables we are going to use

n = 1000000   # it will take some time but with less iteration the result is not as clear
n_dice = 2 #Enjoy changing the number of dice
k = np.zeros(n_dice)
out = []

for i in range(n_dice):
    k[i] = 10**i
    
for i in range(n):
    # roll all the dice
    roll = np.random.choice([0,1,2,3,4,5],n_dice)*k
    # sum the values to get the score
    score = sum(roll)
    out.append(score)

max_value=max(out)
plt.figure(1, dpi = 120)
plt.hist(out, bins = np.arange(0, max_value+2), edgecolor='black')
plt.xlabel("Outcomes")
plt.ylabel("Frequency")
plt.title("Distribution for N relabeled dice ")
plt.show()
