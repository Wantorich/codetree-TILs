year = int(input())

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print('true')
        else :
            print('false')
    else :
        print('true')
else :
    print('false')