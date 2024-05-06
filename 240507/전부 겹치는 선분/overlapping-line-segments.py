n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
arr = [0] * 101
flag = False

for point in points :
    x, y = point
    for i in range(x, y+1) :
        arr[i] += 1

for i in range(len(arr)) :
    if arr[i] == n :
        flag = True
        break

if flag :
    print('Yes')
else :
    print('No')