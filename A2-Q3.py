"""Astro-statistics - Assignment 2: Question 3
   @author: ronaldo"""
   
import numpy as np
import random
import matplotlib.pyplot as plt

n = 100000
r = np.linspace(2,12,11)
count = np.zeros(11)
out = []

def roll_dice(n = 100000):
    
    for i in range(n):
        # Roll each dice
        die1 = random.choice([0,0,0,6,6,6]) # Now our first die is modified
        die2 = random.randint(1, 6)
        
        # Sum the values to get the score
        score = die1 + die2
        out.append(score)
        
        # Conditions to add to the count
        for j in range(len(r)):
            if score == j+2:
                count[j] += 1
    return count/n

probability = roll_dice()
print("Probabilities are: ", np.round(probability*100,2),"%")

plt.figure(1, dpi = 120)
plt.hist(out, bins = np.arange(1, 14), edgecolor='black')
plt.xlabel("Outcomes")
plt.ylabel("Frequency")
plt.title("Distribution for relabeled dice $\{0,0,0,6,6,6\}$ and $\{1,2,3,4,5,6\}$ ")
plt.show()
