n, m = map(int, input().split())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(n) : 
    x, y = tuple(map(int, input().split()))
    arr_2d[x-1][y-1] = x * y

for row in arr_2d :
    for num in row :
        print(num, end=' ')
    print()