
#Part 1. Complete topping module

def addTopBun(toppingStatusList):
    topBunStr = "    ***************    \n ********************* \n***********************"
    toppingStatusList.append(topBunStr)

def addBottomBun(toppingStatusList):
    bottomBunStr = "***********************\n ********************* \n    ***************    "
    toppingStatusList.append(bottomBunStr)

def addPatty(toppingStatusList):
    #function to add patty
    PattyStr = "[======================]"
    toppingStatusList.append(PattyStr)

def addOnion(toppingStatusList):
    #function to add onion
    OnionStr = "[ooooooooooooooooooooo]"
    toppingStatusList.append(OnionStr)

def addCheese(toppingStatusList):
    #function to add cheese
    CheeseStr = "[+++++++++++++++++++++]"
    toppingStatusList.append(CheeseStr)

def addLettuce(toppingStatusList):
    #function to add lettuce
    LettuceStr = "[~~~~~~~~~~~~~~~~~~~~~]"
    toppingStatusList.append(LettuceStr)