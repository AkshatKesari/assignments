import random
for i in range(9):
    a=random.randint(1,100)
    b=random.randint(1,100)
    print('question',i+1,":",a,'x',b,':')
    res=a*b
    resin=int(input('enter your answer:'))
    count=0
    if resin==res:
        print('Right!')
        count+=1
    else:
        print('Wrong!,Correct answer is:',res)
print('your score is:',count,'out of 10')
        
    
