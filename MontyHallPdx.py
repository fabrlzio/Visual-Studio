import random



wins=0



for i in range(10000):
    door=[1,1,1]
    openedDoor=0
    finalChoice=0

    reward= random.randint(0,2)
    door[reward]=2

    choice=random.randint(0,2) 

    while(openedDoor==reward or openedDoor==choice):
        openedDoor+=1

    while(finalChoice==openedDoor or finalChoice==choice):
        finalChoice+=1
  
    if(finalChoice==reward):
        wins+=1

print("\n\nyou won: ", wins)




