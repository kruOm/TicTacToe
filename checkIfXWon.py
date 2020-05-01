# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:59:53 2020
@author: Unmesh
"""

def checkIfXWonHorizontal(topLine,centerLine,bottomLine):
    if topLine['left'] == topLine['center'] == topLine['right'] == 'X':
        print('X won by Top Line')
        return(True)
    elif centerLine['left'] == centerLine['center'] == centerLine['right'] == 'X':
        print('X won by Center Line')
        return(True)
    elif bottomLine['left'] == bottomLine['center'] == bottomLine['right'] == 'X':
        print('X won by Bottom Line')
        return(True)

def checkIfXWonVertical(topLine,centerLine,bottomLine):
    if topLine['left'] == centerLine['left'] == bottomLine['left'] == 'X':
        print('X won by Left Vertical Line')
        return(True)
    elif topLine['center'] == centerLine['center'] == bottomLine['center'] == 'X':
       print('X won by Center Vertical Line')
       return(True)
    elif topLine['right'] == centerLine['right'] == bottomLine['right'] == 'X':
       print('X won by Right Vertical Line')
       return(True)

def checkIfXWonDiagonal(topLine,centerLine,bottomLine):
    if topLine['left'] == centerLine['center'] == bottomLine['right'] == 'X':
        print('X won by Left to Right Diagonal')
        return(True)
    elif topLine['right'] == centerLine['center'] == bottomLine['left'] == 'X':
        print('X won by Left Diagonal')
        return(True)
    
def checkIfXWon(topLine,centerLine,bottomLine):
    if(checkIfXWonHorizontal(topLine, centerLine, bottomLine)) or (checkIfXWonVertical(topLine, centerLine, bottomLine)) or (checkIfXWonDiagonal(topLine, centerLine, bottomLine)):
        return(True)
    else:
        return(False)
    