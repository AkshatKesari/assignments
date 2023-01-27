# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 00:49:25 2023

@author: DELL
"""

for i in range(6):
    for j in range(i):
        print("*",end='')
    print()
for i in range(6):
    for j in range(6-i):
        print("*",end='')
    print()