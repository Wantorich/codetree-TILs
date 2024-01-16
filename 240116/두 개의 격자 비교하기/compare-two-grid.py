n, m = map(int, input().split())
grid_A = [list(map(int, input().split())) for _ in range(n)]
grid_B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if grid_A[i][j] == grid_B[i][j] :
            print(0, end=' ')
        else :
            print(1, end=' ')
    print()