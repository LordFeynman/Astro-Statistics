# we start again by importing the packages

import numpy as np
import matplotlib.pyplot as plt

# define the variables that we are going to need

n = 10000                 # number of simulations
k = 10                      # number of different probabilities that the host knows which is the winning door

# loop to change the probability that the host knows which is the winning door
pr_wc = np.zeros(k)         # in these vectors we are going to save the probabilities of winning for different k
pr_wnc = np.zeros(k)
for j in range(k):
    # define the vectors where we are going to keep trace of the wins (=1) and of the losses (=0)
    wins_c = np.zeros(n)  # changing door
    wins_nc = np.zeros(n)  # not changing door
    # define the vectors where we update the probabilities at each step of the loop
    probwc = np.zeros(n)  # changing door
    probwnc = np.zeros(n)  # not changing door
    for i in range(n):
        know = np.random.choice(range(1, k + 1))
        if know > j:
            c = 0  # in this case the host knows
        else:
            c = 1  # in this case the host doesn't know
        cd = np.random.choice(range(1, 4))          # randomly selecting the chosen door by the player
        wd = np.random.choice(range(1, 4))          # randomly selecting the winning door
        if c == 1:              # if the host doesn't know the winning door we need to specify the opened door
            flag = 0            # defining a flag that we will use for the while loop
            while flag == 0:
                od = np.random.choice(range(1, 4))      # randomly selecting the door opened by the host
                if od != cd:            # the host cannot open the door chosen by the player
                    flag = 1            # change the value of the flag to exit from the while loop
            if (od != wd) and (cd != wd):
                wins_c[i] = 1  # if the initial chosen door is not the winning door, switching the door the player wins
            if cd == wd:
                wins_nc[i] = 1  # the only possibility to win without changing is if initially the chosen door was the
                                # winning door
        else:
            if wd == cd:
                wins_nc[i] = 1  # winning without changing door
            else:
                wins_c[i] = 1  # winning changing door
        # now I have to start to compute the mean from the second value because I need at least two element
        # for sure there is a smarter way to do this, but I don't know it
        if i > 1:
            probwnc[i] = np.mean(wins_nc[:i])  # updated (from 0 to i) probability of winning without changing the door
            probwc[i] = np.mean(wins_c[:i])    # updated (from 0 to i) probability of winning changing the door
        pr_wc[j] = probwc[i]                   # save the probabilities, in the end doing like this we keep memory
        pr_wnc[j] = probwnc[i]                 # only of the last one for each loop over 'i'


# print the results
print("-------------------------------------------------------------------------------------------------------")
print("The probability of winning without changing the door is = ", pr_wnc)
print("The probability of winning changing the door is = ", pr_wc)
print("-------------------------------------------------------------------------------------------------------")

# plot the results
x_plot = np.linspace(1, k, k)

plt.title('Probabilities for non classic Monty Hall')
plt.plot(x_plot, pr_wc, label='Changing Door')
plt.plot(x_plot, pr_wnc, label='Not Changing Door')
plt.legend()
plt.xlabel('k-parameter')
plt.ylabel('Probability')
plt.show()
