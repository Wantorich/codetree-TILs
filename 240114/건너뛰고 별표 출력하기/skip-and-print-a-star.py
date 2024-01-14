n = int(input())

for i in range(1, n+1) :
    for _ in range(i) :
        print('*', end='')
    print()
    print()

for j in range(n-1, 0, -1) :
    for _ in range(j) :
        print('*', end='')
    print()
    print()