size = 19
grid = [list(map(int, input().split())) for _ in range(size)]

# dxs, dys
dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]
winner = 0
center_pos = (-1, -1)

def in_range(x,y) :
    return 0 <= x < size and 0 <= y < size

for i in range(size) :
    for j in range(size) :
        if grid[i][j] == 0 :
            continue
        currX, currY = i, j
        status = grid[i][j]
        cnt = 0
        for dx, dy in zip(dxs, dys) :
            while True :
                nx, ny = currX + dx, currY + dy
                if not in_range(nx, ny) or grid[nx][ny] != status :
                    break
                currX, currY = nx, ny
                cnt += 1
                if cnt >= 4 :
                    winner = status
                    center_pos = (currX - dx*2, currY - dy*2)
                    break
        if winner != 0 :
            break
        
if winner != 0 :
    print(winner)
    print(center_pos[0]+1, center_pos[1]+1)
else :
    print(winner)