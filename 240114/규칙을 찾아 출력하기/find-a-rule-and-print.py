n = int(input())

for i in range(1, n+1) :
    for j in range(1, n+1) :
        half = 2 * i
        if (i == 1 or i == n or j == 1 or j == n) or (i+j < half):
            print('*', end=' ')
        else : 
            print(' ', end=' ')
    print()