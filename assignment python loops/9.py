# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 09:40:20 2023

@author: DELL
"""
#q9
listin=input('enter space seperated words:').split()
setin=set(listin)
for i in setin:
    count=0
    for j in listin:
        if j==i:
            count+=1
    print('number of',i,'=',count)