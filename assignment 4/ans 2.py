year=int(input('enter year:'))
if year%100==0:
    if year%400==0:
        print("its a leap year")
    else:
        print('its not a leap year')
else:
    if year%4==0:
        print("its a leap year")
    else:
        print('its not a leap year')
