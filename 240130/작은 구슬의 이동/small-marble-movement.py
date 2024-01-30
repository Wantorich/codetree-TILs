n, t = map(int, input().split())
r, c, d = input().split()

mapper = {
    'R' : 3,
    'L' : 0,
    'D' : 1,
    'U' : 2
}

dxs, dxy = [0, 1, -1, 0], [-1, 0, 0, 1]
squares = [[0] * n for _ in range(n)]
x, y = int(r)-1, int(c)-1
mov_dir = mapper[d]

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

while t > 0 :
    nx, ny = x + dxs[mov_dir], y + dxy[mov_dir]
    if in_range(nx, ny) :
        x, y = nx, ny
    else :
        mov_dir = 3 - mov_dir
    t -= 1

print(x+1,y+1)