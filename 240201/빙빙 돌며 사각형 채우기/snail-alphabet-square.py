n, m = map(int, input().split())

# dir -> E, S, W, N
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
mov_dir = 0

squares = [[0] * m for _ in range(n)]

def in_range(x, y) :
    return 0 <= x <= n-1 and 0 <= y <= m-1

alpha = 'A'
x, y = 0, 0
for _ in range(m*n) :
    squares[x][y] = alpha
    if alpha == 'Z' :
        alpha = 'A'
    else :
        alpha = chr(ord(alpha) + 1)
    nx, ny = x + dxs[mov_dir], y + dys[mov_dir]
    if in_range(nx, ny) and squares[nx][ny] == 0 :
        x, y = nx, ny
    else :
        mov_dir = (mov_dir + 1) % 4
        x, y = x + dxs[mov_dir], y + dys[mov_dir]
    
for row in range(n) :
    print(' '.join(map(str, squares[row])))