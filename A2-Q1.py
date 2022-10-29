import numpy as np
import random
import matplotlib.pyplot as plt

n = 10000
r = np.linspace(2,12,11)
count = np.zeros(11)

def roll_dice(n = 10000):
    
    for i in range(n):
        # Roll each dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        # Sum the values to get the score
        score = die1 + die2
        
        # Conditions to add to the count
        for j in range(len(r)):
            if score == j+2:
                count[j] += 1
    return count/n

probability = roll_dice()

plt.scatter(r, probability)
plt.show()
#plt.scatter(np.arange(2, 13), roll_dice())
#plt.show()
print("Probabilities are: ", np.round(probability*100,2),"%")