import numpy as np
import matplotlib.pyplot as plt

n = 10000
n_dice2 = 2
n_dice3 = 3
n_dice4 = 4
n_dice10 = 10
n_dice20 = 20

r2 = np.linspace(0,6*n_dice2,6*n_dice2+1)
r3 = np.linspace(0,6*n_dice3,6*n_dice3+1)
r4 = np.linspace(0,6*n_dice4,6*n_dice4+1)
r10 = np.linspace(0,6*n_dice10,6*n_dice10+1)
r20 = np.linspace(0,6*n_dice20,6*n_dice20+1)

count2 = np.zeros(6*n_dice2+1)
count3 = np.zeros(6*n_dice3+1)
count4 = np.zeros(6*n_dice4+1)
count10 = np.zeros(6*n_dice10+1)
count20 = np.zeros(6*n_dice20+1)

def roll_dice2(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll2 = np.random.randint(1,7,n_dice2)
        for i in range(n_dice2):
            score2 = sum(roll2)
        # Sum the values to get the score
        
        # Conditions to add to the count
        for k in range(len(r2)):
            if score2 == k:
                count2[k] += 1
        start += 1
    return count2/n

def roll_dice3(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll3 = np.random.randint(1,7,n_dice3)
        for i in range(n_dice3):
            score3 = sum(roll3)
        # Sum the values to get the score
        
        # Conditions to add to the count
        for k in range(len(r3)):
            if score3 == k:
                count3[k] += 1
        start += 1
    return count3/n

def roll_dice4(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll4 = np.random.randint(1,7,n_dice4)
        for i in range(n_dice4):
            score4 = sum(roll4)
        # Sum the values to get the score
        
        # Conditions to add to the count
        for k in range(len(r4)):
            if score4 == k:
                count4[k] += 1
        start += 1
    return count4/n

def roll_dice10(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll10 = np.random.randint(1,7,n_dice10)
        for i in range(n_dice10):
            score10 = sum(roll10)
        # Sum the values to get the score
        
        # Conditions to add to the count
        for k in range(len(r10)):
            if score10 == k:
                count10[k] += 1
        start += 1
    return count10/n

def roll_dice20(n = 10000):
    start = 1
    while start < n:
        # Roll each dice
        roll20 = np.random.randint(1,7,n_dice20)
        for i in range(n_dice20):
            score20 = sum(roll20)
        # Sum the values to get the score
        
        # Conditions to add to the count
        for k in range(len(r20)):
            if score20 == k:
                count20[k] += 1
        start += 1
    return count20/n

probability2 = roll_dice2()
probability3 = roll_dice3()
probability4 = roll_dice4()
probability10 = roll_dice10()
probability20 = roll_dice20()

#fig, (ax1, ax2) = plt.subplots(1, 2)
#fig.suptitle('Horizontally stacked subplots')
#ax1.scatter(r2, probability2, s=5)
#ax2.scatter(r3, probability3, s=5)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Probability Distribution for N dice throws')
axes[0,0].scatter(r2, probability2, s=5)
axes[0, 0].set_title('Two dice')
axes[0,1].scatter(r3, probability3, s=5)
axes[0, 1].set_title('Three dice')
axes[1,0].scatter(r4, probability4, s=5)
axes[1, 0].set_title('Four dice')
axes[1,1].scatter(r10, probability10, s=5)
axes[1, 1].set_title('Ten dice')

for ax in axes.flat:
    ax.set(xlabel='$X$', ylabel='$P(X)$')
#for ax in axes.flat:
#    ax.label_outer()

fig.tight_layout()
plt.show()

