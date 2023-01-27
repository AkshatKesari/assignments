# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:10:55 2023

@author: DELL
"""
#divisibility of numbers in user input range by given number
op=int(input('enter range opening:'))
cl=int(input('enter range closing:'))
n=int(input('enter number n:'))
print('Numbers in a Range Divisible by a Given Number n:')
for i in range(op,cl+1):
    if i%n==0:
        print(i)