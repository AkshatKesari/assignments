# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:14:41 2023

@author: DELL
"""

def perfect(n):
    if n<=0:
        return False
    else:
        sumn=0
        for i in range(1,n):
            if n%i==0:
                sumn+=i
        if sumn==n:
            return True
#finding perfect numbers in the range
l=[]
for i in range(1,int(input('enter range closing:'))):
    if perfect(i):
        l.append(i)
print(l)