#assignment 2
#q1a
str1='python is a case sensitive language'
print(len(str1))
#q1b
print(str1[::-1])
#q1c
str3=str1[10:26]
print(str3)
#q1d
str4=str1[:9]+' object oriented '+str1[27:]
print(str4)
#q1e
print(str1.index('a'))
#q1f
str4=""
for i in str1:
    if i==" ":
        pass
    else:
        str4+=i
print(str4)



