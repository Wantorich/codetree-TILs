commands = input()

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3 # 북쪽 바라보고 시작

# L이면 왼쪽으로 90도 -> dir_num -1
# R이면 오른쪽으로 90도 -> dir_num + 1
# F면 앞으로 한칸 전진

for command in commands :
    if command == 'L' :
        dir_num = (dir_num - 1 + 4) % 4
    elif command == 'R' :
        dir_num = (dir_num + 1) % 4
    else :
        x, y = x + dx[dir_num], y + dy[dir_num]    

print(x,y)