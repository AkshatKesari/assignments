#q2
gross=int(input("enter gross income:"))
nod=int(input("enter number of dependents:"))
taxincome=gross-10000-nod*3000
tax=taxincome*20/100
print(tax)
