# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:44:37 2020

@author: Unmesh
"""

def printOutput(inputLine):
    outputString =''
    for everyCorner,everyItem in inputLine.items():
        if everyCorner == 'right':
            outputString += everyItem  
        else:
            outputString += everyItem + '|'
    print(outputString)

def printLines():
    print('- - -')

def printTicTacToe(topLine,centerLine,bottomLine):
    printOutput(topLine)
    printLines()
    printOutput(centerLine)
    printLines()
    printOutput(bottomLine)
    
