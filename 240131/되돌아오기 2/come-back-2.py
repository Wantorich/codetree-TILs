command = input()
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 3 # North
mapper = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}
x, y = 0, 0
time, res = 0, -1
for mov_dir in command :
    if mov_dir == 'R' or mov_dir == 'L':
        dir_num = (dir_num + 1) % 4 if mov_dir == 'R' else (dir_num - 1 + 4) % 4
        time += 1
        continue
    mov_idx = dir_num
    nx, ny = x + dxs[mov_idx], y + dys[mov_idx]
    time += 1
    if nx == 0 and ny == 0 :
        res = time
        break
    x, y = nx, ny

print(res)