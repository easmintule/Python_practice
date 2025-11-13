a = int(input('intput a year : '))

if a % 4 == 0 :
    if a % 100 == 0:
        if a % 400 == 0 :
            print('Leap year')
        else:print('not leap year')

    else:print('leap year')
else :
    print('not Leap year')
