n = int(input())
for i in range(2*n) :
    if i % 2 == 1 :
        star = n - (i - 1) / 2
    else :
        star = 1 + (i / 2)
    for _ in range(int(star)) :
        print('*', end=' ')
    print()