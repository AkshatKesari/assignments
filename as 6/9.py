# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 21:05:28 2023

@author: DELL
"""

#q9
class Parentheses:
    def __init__(self, string):
        self.string = string
    
    def is_valid(self):
        stack = []
        for char in self.string:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in [")", "}", "]"]:
                if not stack:
                    return False
                current_char = stack.pop()
                if char == ")" and current_char != "(":
                    return False
                elif char == "}" and current_char != "{":
                    return False
                elif char == "]" and current_char != "[":
                    return False
        return not stack

# Test the class
string1 = "()"
string2 = "()[]{}"
string3 = "[)"
string4 = "({[)]"
string5 = "{{{"

p1 = Parentheses(string1)
p2 = Parentheses(string2)
p3 = Parentheses(string3)
p4 = Parentheses(string4)
p5 = Parentheses(string5)

print(p1.is_valid())
print(p2.is_valid())
print(p3.is_valid())
print(p4.is_valid())
print(p5.is_valid())