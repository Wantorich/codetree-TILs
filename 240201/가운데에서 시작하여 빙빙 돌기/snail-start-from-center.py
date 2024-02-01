# 가운데 좌표는 n/2, n/2
# 정사각형이니 가운데를 제외하고 양쪽이 n/2 n/2길이만큼 남아있음
# 방향은 E N W S
# 1 1 2 2 
# 3 3 4 4
# 5 5 6 6
# 거꾸로 채우기? 오른쪽 아래부터?

n = int(input())

# dir -> W N E S
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
mov_dir = 0

squares = [[0] * n for _ in range(n)]

def in_range(x, y) :
    return 0 <= x <= n-1 and 0 <= y <= n-1

num = n*n
x, y = n-1, n-1
for _ in range(n*n) :
    squares[x][y] = num
    num -= 1
    nx, ny = x + dxs[mov_dir], y + dys[mov_dir]
    if in_range(nx, ny) and squares[nx][ny] == 0 :
        x, y = nx, ny
    else :
        mov_dir = (mov_dir + 1) % 4
        x, y = x + dxs[mov_dir], y + dys[mov_dir]
    
for row in range(n) :
    print(' '.join(map(str, squares[row])))