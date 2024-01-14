n = int(input())
for i in range(1, 2*n) :
    if i < n :
        for k in range(n-i) :
            print(' ', end=' ')
        for _ in range(i) :
            print('@', end=' ')
    elif i > n :
        for _ in range(2*n-i) :
            print('@', end=' ')
        for k in range(i-n) :
            print(' ', end=' ')
    else :
        for _ in range(n) :
            print('@', end=' ')
    print()