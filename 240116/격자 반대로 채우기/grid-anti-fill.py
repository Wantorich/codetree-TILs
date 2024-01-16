n = int(input())
num = 1
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for j in range(n-1, -1, -1) :
    if (n % 2 == 0 and j % 2 == 1) or (n % 2 == 1 and j % 2 == 0) :
        for i in range(n-1, -1, -1) :
            arr_2d[i][j] = num
            num += 1
    else :
        for i in range(n) :
            arr_2d[i][j] = num
            num += 1

for row in arr_2d :
    for num in row :
        print(num, end=' ')
    print()