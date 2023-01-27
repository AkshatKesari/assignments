#q8
listin=input('enter space seperated 10 integers:').split()
for i in range(len(listin)):
    listin[i]=int(listin[i])
pos=[]
neg=[]
odd=[]
even=[]
setin=set(listin)
for i in listin:
    if i>0:
        pos.append(i)
    if i<0:
        neg.append(i)
    if i%2==1:
        odd.append(i)
    if i%2==0:
        even.append(i)
for i in setin:
    count=0
    for j in listin:
        if i==j:
            count+=1
    print('number of',i,'=',count)
print('positive numbers in input:',pos)
print('negative numbers in input:',neg)
print('odd numbers in input:',odd)
print('even numbers in input:',even)    
