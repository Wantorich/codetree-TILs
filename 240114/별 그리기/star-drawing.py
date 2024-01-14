n = int(input())
for i in range(1, 2*n) :
    if i < n :
        for _ in range(n-i) :
            print(' ', end='')
        for _ in range(2*i-1) :
            print('*', end='')
    elif i > n :
        for _ in range(i-n) :
            print(' ', end='')
        for _ in range(2*n-1-2*(i-n)) :
            print('*', end='')
    else :
        for _ in range(2*i-1) :
            print('*', end='')
    print()