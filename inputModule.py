# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:36:09 2020

@author: Unmesh
"""

import updateList as moduleupdateList

proceedOrInputAgain = 0
listOfChoices = [0]

def takeInput(XOrO):
    inputString = XOrO
    x = input(inputString)
    try:
        x = int(x)
    except:
        x=10    
    return(x)

def startTheGame(xplay,oplay,topLine,centerLine,bottomLine):
    localTakeInput = 0
    if xplay == True and oplay==False:
        localTakeInput = takeInput('X Please enter a number ? ')
        while (localTakeInput in listOfChoices) or localTakeInput <1 or localTakeInput>9:
            localTakeInput = takeInput('Invalid input. X Please enter another number between 1 and 9 which is not taken? ')
        else: 
            listOfChoices.append(localTakeInput)    
            print(listOfChoices)    
            moduleupdateList.updateList(topLine,centerLine,bottomLine,localTakeInput,'X') 
            
    if xplay == False and oplay == True:
        localTakeInput = takeInput('O Please enter a number ? ')
        while (localTakeInput in listOfChoices) or localTakeInput <1 or localTakeInput>9:
            localTakeInput = takeInput('Invalid input. O Please enter another number betweeen 1 and 9 which is not taken? ')
        else: 
            listOfChoices.append(localTakeInput)    
            print(listOfChoices)    
            moduleupdateList.updateList(topLine,centerLine,bottomLine,localTakeInput,'O') 



def checkForDraw():
    if len(listOfChoices)==10:
        print('The Game is a draw')
        return(True)
    else:
        return(False)
    