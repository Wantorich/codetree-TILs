import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
min_dis = sys.maxsize

for i in range(n) :
    for j in range(i+1, n) :
        x1, y1 = points[i]
        x2, y2 = points[j]
        dis = ((x2-x1) ** 2) + ((y2-y1) ** 2)
        min_dis = min(min_dis, dis)

print(min_dis)