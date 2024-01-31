n = int(input())
squares = [[0] * (n+2) for _ in range(n+2)]

for i in range(1, n+1) :
    slash = list(input())
    for j in range(1, n+1) :
        squares[i][j] = slash[j-1]

k = int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] # S W N E

x, y = 0, 0
circuit = 3
for _ in range(k) :
    nx, ny = x + dxs[circuit], y + dys[circuit]
    if (nx == 0 and ny == n+1) or (nx == n+1 and ny == n+1) and (nx == n+1 and ny == 0) :
        circuit = (circuit + 1) % 4
        nx, ny = nx + dxs[circuit], ny + dys[circuit]
    x, y = nx, ny
    
# 0 1 2 3 -(> S W N E
dir_num = (k - 1) // n # init dir
# init = k % n + dir_num * n
# if dir_num == 0 :
#     x, y = 0, k+1
# elif dir_num == 1 :
#     x, y = k % n + dir_num, n+1
# elif dir_num == 2 :
#     x, y = n+1, init
# else :
#     x, y = init, 0

def in_range(x,y) :
    return 1 <= x <= n and 1 <= y <= n

cnt = 0
x, y = x + dxs[dir_num], y + dys[dir_num]
while in_range(x,y) :
    if (squares[x][y] == "\\" and dir_num % 2 == 0) or (squares[x][y] == "/" and dir_num % 2 == 1) :
        dir_num = (dir_num - 1 + 4) % 4
    else :
        dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    cnt += 1

print(cnt)