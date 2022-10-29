import numpy as np
import matplotlib.pyplot as plt

n = 10000
n_dice = 100
r = np.linspace(0,6*n_dice,6*n_dice+1)
die = np.zeros(n_dice)
count = np.zeros(6*n_dice+1)

def roll_dice(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll = np.random.randint(1,7,n_dice)
        for i in range(n_dice):
            score = sum(roll)
        # Sum the values to get the score
        
        # Conditions to add to the count
        for k in range(len(r)):
            if score == k:
                count[k] += 1
        start += 1
    return count/n

probability = roll_dice()
print(probability)

plt.figure(1, dpi = 120)
plt.scatter(r, probability, s=5)
plt.xlabel("$X$")
plt.ylabel("$P(X)$")
plt.title("Probability distribution for the sum of 100 dice")
plt.show()