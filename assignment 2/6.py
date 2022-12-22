len1 = float(input("Enter length of side 1: "))
len2 = float(input("Enter length of side 2: "))
len3 = float(input("Enter length of side 3: "))
if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
    print("Yes")
else:
    print("No")
