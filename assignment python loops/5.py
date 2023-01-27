# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 01:15:26 2023

@author: DELL
"""

n = int(input("Enter number of rows: "))
a = 65
for i in range (n+1):
    for j in range (i):
        print (chr(a), end = "")
        a = a + 1
        if a>=91:
            a = a-26
    print("")