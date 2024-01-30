n = int(input())

squares = [[0] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

for row in range(n) :
    cols = list(map(int, input().split()))
    for col in range(n) :
        squares[row][col] = cols[col]

cnt = 0
for row in range(n) :
    for col in range(n) :
        sb_cnt = 0
        for dx, dy in zip(dxs, dys) :
            nx, ny = row + dx, col + dy
            if in_range(nx, ny) and squares[nx][ny] == 1 :
                sb_cnt += 1 
        if sb_cnt >= 3 :
            cnt += 1

print(cnt)