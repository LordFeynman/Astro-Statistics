# we start again by importing the packages

import numpy as np
import matplotlib.pyplot as plt

# define the variables that we are going to need

# NEED TO CANCEL THE PART OF CW1 AND CW2 WHICH IS NOW UNNECESSARY

n = 100000                  # number of simulations

# define the vectors where we are going to keep trace of the wins (=1) and of the losses (=0)
wins_c = np.zeros(n)        # changing door
wins_nc = np.zeros(n)       # not changing door
# define the vectors where we update the probabilities at each step of the loop
probwc = np.zeros(n)        # changing door
probwnc = np.zeros(n)       # not changing door

# loop to simulate each game

for i in range(n):
    cd = np.random.choice(range(1, 4))          # randomly selecting the chosen door by the player
    wd = np.random.choice(range(1, 4))          # randomly selecting the winning door
    flag = 0                                    # defining a flag that we will use for the while loop
    while flag == 0:
        od = np.random.choice(range(1, 4))      # randomly selecting the door opened by the host
        if od != cd:            # the host cannot open the door chosen by the player
            flag = 1            # change the value of the flag to exit from the while loop
    if od == wd:
        wins_c[i] = 1           # if the host opens the winning door, switching the door the player wins
    if cd != wd:
        wins_c[i] = 1           # if the initial chosen door is not the winning door, switching the door the player wins
    if cd == wd:
        wins_nc[i] = 1          # the only possibility to win without changing is if initially the chosen door was the
                                # winning door
    # in my opinion the first of the last three "if" is not necessary since the other two do the job.
    # if the initial door is not the one with the car, the player always wins if changes the door, whatever the host
    # opens, assuming he can choose the opened door if it reveals the car.
    # now same if of the previous exercise
    if i > 1:
        probwnc[i] = np.mean(wins_nc[:i])  # updated (from 0 to i) probability of winning without changing the door
        probwc[i] = np.mean(wins_c[:i])  # updated (from 0 to i) probability of winning changing the door

# print the results
print("The probability of winning without changing the door is = ", probwnc[n - 1])
print("The probability of winning changing the door is = ", probwc[n - 1])

# now we need to plot the results

# first I define the 'x' vector (shouldn't be necessary, but it doesn't work either way)
x_plot = np.linspace(1, n, n)

plt.title('Probabilities for classic Monty Hall')
plt.plot(x_plot, probwc, label='Changing Door')
plt.plot(x_plot, probwnc, label='Not Changing Door')
plt.legend()
plt.xlabel('Number of Iterations')
plt.ylabel('Probability')
plt.show()
