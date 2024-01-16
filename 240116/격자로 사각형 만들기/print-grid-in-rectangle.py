n = int(input())

# arr_2d = [[0 for _ in range(n)] for in range(n)]
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n) :
    for j in range(n) :
        if i == 0 or j == 0:
            arr_2d[i][j] = 1
            print(1, end=' ')
        else :
            arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i-1][j] + arr_2d[i][j-1]
            print(f'{arr_2d[i][j]}', end=' ')
    print()