n, t = map(int, input().split())
commands = input()
squares = [list(map(int, input().split())) for _ in range(n)]

# dir -> W N E S
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
mov_dir = 1

def in_range(x, y) :
    return 0 <= x <= n-1 and 0 <= y <= n-1

total = 0
x, y = n // 2, n // 2
total += squares[x][y]
for command in commands :
    if command == 'R' :
        mov_dir = (mov_dir + 1) % 4
    elif command == 'L' :
        mov_dir = (mov_dir - 1 + 4) % 4
    else :
        nx, ny = x + dxs[mov_dir], y + dys[mov_dir]
        if in_range(nx, ny) :
            x, y = nx, ny
            total += squares[x][y]

print(total)