# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:21:42 2020

@author: Unmesh
"""
topLine = {'left':' ','center':' ','right':' '}
centerLine = {'left':' ','center':' ','right':' '}
bottomLine = {'left':' ','center':' ','right':' '}

import checkIfXWon as modulecheckIfXWon
import checkIfOWon as modulecheckIfOWon 
import inputModule as moduleinputModule
import printTicTacToe as moduleprintTicTacToe

xplay=True
oplay=False
gameover=False

while gameover==False:
    moduleinputModule.startTheGame(xplay,oplay,topLine,centerLine,bottomLine)
    moduleprintTicTacToe.printTicTacToe(topLine,centerLine,bottomLine)
    gameover=modulecheckIfXWon.checkIfXWon(topLine,centerLine,bottomLine)
    if (gameover):
        break
    if (moduleinputModule.checkForDraw()):
        break
    xplay = False
    oplay = True
    moduleinputModule.startTheGame(xplay,oplay,topLine,centerLine,bottomLine)
    moduleprintTicTacToe.printTicTacToe(topLine,centerLine,bottomLine)
    gameover=modulecheckIfOWon.checkIfOWon(topLine,centerLine,bottomLine)
    if (gameover):
        break
    xplay = True
    oplay = False

        
    