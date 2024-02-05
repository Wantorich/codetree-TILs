n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

# target = 'LEE'

# def in_range(x,y) :
#     return 0 <= x < n and 0 <= y < m

# def is_exist(x,y) :
#     exist = False
#     if grid[x][y] == 'L' :

cnt = 0

for i in range(n) :
    for j in range(m-2) :
        if grid[i][j] == 'L' and grid[i][j+1] == 'E' and grid[i][j+2] == 'E' \
        or grid[i][j] == 'E' and grid[i][j+1] == 'E' and grid[i][j+2] == 'L' :
            cnt += 1

for i in range(n-2) :
    for j in range(m) :
        if grid[i][j] == 'L' and grid[i+1][j] == 'E' and grid[i+2][j] == 'E' \
        or grid[i][j] == 'E' and grid[i+1][j] == 'E' and grid[i+2][j] == 'L' :
            cnt += 1

for i in range(n-2) :
    for j in range(m-2) :
        if grid[i][j] == 'L' and grid[i+1][j+1] == 'E' and grid[i+2][j+2] == 'E' \
        or grid[i][j] == 'E' and grid[i+1][j+1] == 'E' and grid[i+2][j+2] == 'L' :
            cnt += 1

for i in range(2, n) :
    for j in range(m-2) :
        if grid[i][j] == 'L' and grid[i-1][j+1] == 'E' and grid[i-2][j+2] == 'E' \
        or grid[i][j] == 'E' and grid[i-1][j+1] == 'E' and grid[i-2][j+2] == 'L' :
            cnt += 1

print(cnt)