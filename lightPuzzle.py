
print("Puzzle: Turn on all the lights!\n")

lightList = [False, False, False, False]

#Part 1. write a condition that will be True while working on the puzzle:
while lightList[0] == False or lightList[1] == False or lightList[2] == False or lightList[3] == False:


    #Part 2. Get keyboard input from user. 
    #User will input 0 for 1st button, 1 for 2nd button, and 2 for 3rd button. 

    select_button = int(input("select button (0:1st button, 1:2nd button, 2:3rd button): "))

    #Part 3. Turn on/off lights based on the selected button.
    if select_button == 0:
        if lightList[0] == False:
            lightList[0] = True #turn on light
        else:
            lightList[0] = False   

    elif select_button == 1:
        if lightList[1] == False:
            lightList[1] = True    
        else:
            lightList[1] = False
        if lightList[2] == False:
            lightList[2] = True    
        else:
            lightList[2] = False
    
        
    elif select_button == 2:
        if lightList[3] == False:
            lightList[3] = True
        else:
            lightList[3] = False
        if lightList[0] == False:
            lightList[0] = True
        else:
            lightList[0] = False

    print("Current light status:")
    lightStatus= " "
    for i in lightList:
        if i == True:
            lightStatus = lightStatus + "O"
        else:
            lightStatus = lightStatus + "X"
    print(lightStatus)
    
    


    #Part 4. Display light-status using O and X characters. 
    #O denotes that the corresponding light is turned on.
    #X denotes that the corresponding light is turned off.
    

    print()

print("Yes! you've solved the puzzle.")