# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 23:58:38 2023

@author: DELL
"""
#q6
op,cl=input('enter space seperated opening and closing of range:').split()
op,cl=int(op),int(cl)
for i in range(op,cl):
    a=0
    for j in range(2,i):
        if i%j==0:
            a=1
            break
    if i==1:
        a=1
    if a==0:
        print(i)
print('done')
        
        
            