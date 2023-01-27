# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:02:23 2023

@author: DELL
"""
strin=input('enter string to be reversed:')
strout=''
for i in range(1,len(strin)+1):
    strout+=strin[-i]
print(strout)


    