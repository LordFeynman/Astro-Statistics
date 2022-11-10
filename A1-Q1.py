# Solution to the last point of Assignment #1
from typing import Union, Tuple, Optional

import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

# define the variables that we are going to need

# NEED TO CANCEL THE PART OF CW1 AND CW2 WHICH IS NOW UNNECESSARY

n = 100000        # number of simulations

# define the vectors where we are going to keep trace of the wins (=1) and of the losses (=0)
Wins_c = np.zeros(n)        # changing door
Wins_nc = np.zeros(n)       # not changing door
# define the vectors where we update the probabilities at each step of the loop
probwc = np.zeros(n)        # changing door
probwnc = np.zeros(n)       # not changing door

# loop to simulate each game

for i in range(n):
    wd = np.random.choice(range(1, 4))      # chose randomly the winning door
    cd = np.random.choice(range(1, 4))      # chose randomly the player initial door
    # at this point of the game the host opens the third door with a goat behind.
    # if the chosen door is the one with the car and the player doesn't change the door he wins, otherwise he loose and
    # vice versa
    if wd == cd:
        Wins_nc[i] = 1                         # winning without changing door
    else:
        Wins_c[i] = 1                          # winning changing door
# now I have to start to compute the mean from the second value because I need at least two element
# for sure there is a smarter way to do this, but I don't know it
    if i > 1:
        probwnc[i] = np.mean(Wins_nc[:i])  # updated (from 0 to i) probability of winning without changing the door
        probwc[i] = np.mean(Wins_c[:i])  # updated (from 0 to i) probability of winning changing the door


print("The probability of winning without changing the door is = ", probwnc[n-1])
print("The probability of winning changing the door is = ", probwc[n-1])

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
