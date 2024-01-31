n = int(input())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
mapper = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}
x, y = 0, 0
time, res = 0, -1
for _ in range(n) :
    mov_dir, dis = input().split()
    mov_idx = mapper[mov_dir]
    for _ in range(int(dis)) :
        nx, ny = x + dxs[mov_idx], y + dys[mov_idx]
        time += 1
        if nx == 0 and ny == 0 :
            res = time
            break
        x, y = nx, ny
    if res != -1 :
        break

print(res)