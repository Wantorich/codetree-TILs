n = int(input())

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direct = ['E', 'S', 'W', 'N']

for _ in range(n) :
    dir_, dis = input().split()
    idx = direct.index(dir_)
    x, y = x + dx[idx] * int(dis), y + dy[idx] * int(dis)

print(x,y)