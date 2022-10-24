import random
#import matplotlib.pyplot as plt
#import numpy as np

######################## HOST KNOWS WHERE THE PRIZE IS ########################

def standard_monty(doors):
    return random.choice([d for d in doors if d != 0])

def switch_contestant():
    doors = [0,1,2]                             
    init_choice = random.choice(doors)          
    doors.remove(init_choice)                   
    reveal_door = standard_monty(doors)         
    if reveal_door == 0:                             
        return switch_contestant()
    return init_choice != 0 

def stay_contestant():
    doors = [0,1,2]                             
    init_choice = random.choice(doors)          
    doors.remove(init_choice)                   
    reveal_door = standard_monty(doors)         
    if reveal_door == 0:                             
        return stay_contestant()
    return init_choice == 0 

switch_win_s = 0
stay_win_s = 0
n = 10000

#N = np.linspace(0, 100, 101)

for _ in range(n):
    if switch_contestant():
        switch_win_s += 1
    if stay_contestant():
        stay_win_s += 1
print('STANDARD MONTY HALL - QUESTION 1')
print('Switching contestant: %.2f%%' % (float(switch_win_s) / n * 100))
print('Stubborn contestant: %.2f%%' % (float(stay_win_s) / n * 100))
print('\n')

#################### HOST DOES NOT KNOW WHERE THE PRIZE IS ####################

def modified_monty(doors):
    return random.choice(doors)

def switch_cont():
    doors = [0,1,2]                             
    init_choice = random.choice(doors)          
    doors.remove(init_choice)                   
    reveal_door = modified_monty(doors)         
    if reveal_door == 0:                             
        return switch_cont()
    return init_choice != 0 

def stay_cont():
    doors = [0,1,2]                             
    init_choice = random.choice(doors)          
    doors.remove(init_choice)                   
    reveal_door = modified_monty(doors)         
    if reveal_door == 0:                             
        return stay_cont()
    return init_choice == 0 

switch_win_m = 0
stay_win_m = 0

for _ in range(n):
    if switch_cont():
        switch_win_m += 1
    if stay_cont():
        stay_win_m += 1
print('MODIFIED MONTY HALL - QUESTION 2')
print('Switching contestant: %.2f%%' % (float(switch_win_m) / n * 100))
print('Stubborn contestant: %.2f%%' % (float(stay_win_m) / n * 100))

#num_test = []
#win_rate = []
#switch = True
#for i in range(n):
#    num_test.append(i)
#    y = 