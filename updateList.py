# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:19:19 2020

@author: Unmesh
"""

def updateList(topLine,centerLine,bottomLine,x,inputString):
    x=int(x)
    if x==1:
        topLine['left']=inputString
    elif x==2:
        topLine['center']=inputString
    elif x==3:
        topLine['right']=inputString
            
    elif x==4:
        centerLine['left']=inputString
    elif x==5:
        centerLine['center']=inputString
    elif x==6:
        centerLine['right']=inputString

    elif x==7:
        bottomLine['left']=inputString
    elif x==8:
        bottomLine['center']=inputString
    elif x==9:
        bottomLine['right']=inputString
