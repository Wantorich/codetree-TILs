n, m = map(int, input().split())
arr_2d = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

for _ in range(n) : 
    x, y = tuple(map(int, input().split()))
    arr_2d[x][y] = x * y

for row in arr_2d[1:] :
    for num in row[1:] :
        print(num, end=' ')
    print()