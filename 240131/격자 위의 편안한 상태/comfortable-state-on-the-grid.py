n, m = map(int, input().split())
squares = [[0] * (n+1) for _ in range(n+1)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x,y) :
    return 1 <= x <= n and 1 <= y <= n

def is_in_comfort(x,y) :
    cnt = 0
    for dx, dy in zip(dxs, dys) :
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and squares[nx][ny] == 1 :
            cnt += 1
    return True if cnt == 3 else False

for _ in range(m) :
    x, y = map(int, input().split())
    squares[x][y] = 1
    result = 1 if is_in_comfort(x,y) else 0
    print(result)