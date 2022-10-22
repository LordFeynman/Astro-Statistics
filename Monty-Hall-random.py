from numpy import random
import numpy as np
import time

def MontyHallSimulation (N):
    ChoiceUnchanged=[]
    ChoiceChanged=[]
    NN=1
    for i in range(0,N):
        
        # 1) The car is placed behind a random door.
        WinningDoor = random.choice(['Door 1', 'Door 2', 'Door 3'])

        # 2) The contestant selects a random door.
        FirstSelection = random.choice(['Door 1', 'Door 2', 'Door 3'])
        
        # 3) The host opens a door that is different than the contestants choice 
        #    and it is the winning door.
        HostWins = list(set(['Door 1', 'Door 2', 'Door 3']) - set([FirstSelection]))[0]
        ChoiceChanged.append(HostWins==WinningDoor)
        
        # 4) The host opens a door that is different than the contestants choice
        #    and it has a goat
        HostOpens = list(set(['Door 1', 'Door 2', 'Door 3'])-set([FirstSelection]))[0]
        
        # 5) The other door is not the participant's selected door and not the opened door. 
        OtherDoor = list(set(['Door 1', 'Door 2', 'Door 3'])-set([FirstSelection,HostOpens]))[0]
        
        # 6) Add "True" to a list where the participant DOES NOT change their selection AND their 
        #    selection identified the door with the car. 
        ChoiceUnchanged.append(FirstSelection==WinningDoor)
        
        # 7) Add "True" to a list where the participant DOES change their selection and their 
        #    new selected door has the car behind it.
        ChoiceChanged.append(OtherDoor==WinningDoor)
        
    # NOTE: The boolean object "TRUE" is equal to 1 and "False" is equal to 0.
    #       As such, we can use the "sum" function to get the total number of wins
    #       for each strategy.
    print(f'\n\
    {N:,} games were played \n\
    Chances of winning the car based on the following strategies:\n\
    Remaining with initial selection: {"{:.1%}".format(sum(ChoiceUnchanged)/N)}\n\
    Switching doors: {"{:.1%}".format(sum(ChoiceChanged)/N)}')
            
###############################            
###### Run the Simulation######
###############################
Start_time = time.time()
MontyHallSimulation(N=100000)         
print(f'\nSimulation Completed in: {round(time.time()-Start_time,2)} Seconds')