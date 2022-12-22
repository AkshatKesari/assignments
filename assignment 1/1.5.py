#q5
import math
for i in range (24):
    a=(math.sin(15*i*2*math.pi/360)*10000)//1
    b=(math.cos(15*i*2*math.pi/360)*10000)//1
    print(i*15,"---",a,b)
