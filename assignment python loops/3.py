import math
sides=[]
for i in input('enter space seperated sides of triangle:').split():
    sides.append(int(i))
if sides[0]>sides[1]+sides[2] or sides[1]>sides[2]+sides[0] or sides[2]>sides[1]+sides[0]:
    print("triangle could not be formed!")
else:
    print("triangle can be formed")
    area=math.sqrt(sum(sides)/2)
    for i in sides:
        area*=math.sqrt(sum(sides)/2-i)
    print ('area of trianle formed',area)
