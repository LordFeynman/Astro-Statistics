"""Astro-statistics - Assignment 2: Question 1
   @author: ronaldo"""

import numpy as np
import random
import matplotlib.pyplot as plt

n = 100000
r = np.linspace(2,12,13)
count = np.zeros(13)
out = []

def roll_dice(n = 100000):
    
    for i in range(n):
        # Roll each dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        # Sum the values to get the score
        score = die1 + die2
        out.append(score)
        
        # Conditions to add to the count
        for j in range(len(r)):
            if score == j:
                count[j] += 1
    return count/n

probability = roll_dice()
print("Probabilities are: ", np.round(probability*100,2),"%")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
fig.suptitle('Probability Distribution')
ax1.scatter(r, probability)
ax1.set_title('Scatter Plot')
ax1.set(xlabel='$X$', ylabel='$P(X)$')
ax2.hist(out, bins = np.arange(2, 14), edgecolor='black')
ax2.set_title('Histrogram')
ax2.set(xlabel='Outcome', ylabel='Frequency')

fig.tight_layout()
plt.show()
