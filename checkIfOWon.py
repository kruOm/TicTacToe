# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:16:52 2020

@author: Unmesh
"""
def checkIfOWonHorizontal(topLine,centerLine,bottomLine):
    if topLine['left'] == topLine['center'] == topLine['right'] == 'O':
        print('O won by Top Line')
        return(True)
    elif centerLine['left'] == centerLine['center'] == centerLine['right'] == 'O':
        print('O won by Center Line')
        return(True)
    elif bottomLine['left'] == bottomLine['center'] == bottomLine['right'] == 'O':
        print('O won by Bottom Line')
        return(True)

def checkIfOWonVertical(topLine,centerLine,bottomLine):
    if topLine['left'] == centerLine['left'] == bottomLine['left'] == 'O':
        print('O won by Left Vertical Line')
        return(True)
    elif topLine['center'] == centerLine['center'] == bottomLine['center'] == 'O':
        print('O won by Center Vertical Line')
        return(True)
    elif topLine['right'] == centerLine['right'] == bottomLine['right'] == 'O':
        print('O won by Right Vertical Line')
        return(True)
    
def checkIfOWonDiagonal(topLine,centerLine,bottomLine):
    if topLine['left'] == centerLine['center'] == bottomLine['right'] == 'O':
        print('O won by Left to Right Diagonal')
        return(True)
    elif topLine['right'] == centerLine['center'] == bottomLine['left'] == 'O':
        print('O won by Left Diagonal')
        return(True)
    
def checkIfOWon(topLine,centerLine,bottomLine):
    if(checkIfOWonHorizontal(topLine, centerLine, bottomLine)) or (checkIfOWonVertical(topLine, centerLine, bottomLine)) or (checkIfOWonDiagonal(topLine, centerLine, bottomLine)):
        return(True)
    else:
        return(False)