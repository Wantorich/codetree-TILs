n = int(input())
for i in range(1, 2*n) :
    if i < n :
        for _ in range(n-i) :
            print(' ', end='')
        for k in range(2*i-1) :
            if k % 2 == 0 :
                print('*', end='')
            else :
                print(' ', end='')
    elif i > n :
        for _ in range(i-n) :
            print(' ', end='')
        for k in range(2*n-1-2*(i-n)) :
            if k % 2 == 0 :
                print('*', end='')
            else :
                print(' ', end='')
    else :
        for k in range(2*i-1) :
            if k % 2 == 0 :
                print('*', end='')
            else :
                print(' ', end='')
    print()