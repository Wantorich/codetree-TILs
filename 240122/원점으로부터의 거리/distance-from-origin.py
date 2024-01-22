def cmp_dist(x1, y1, x2, y2) :
    return abs(x1-x2) + abs(y1-y2)

n = int(input())
points = []
for i in range(1, n+1) :
    x, y = tuple(map(int, input().split()))
    points.append((x, y, i))

# points = [tuple(map(int, input().split())) for _ in range(n)]
# print(points)

points.sort(key=lambda point : cmp_dist(point[0], point[1], 0, 0))
for _, _, idx in points :
    print(idx)

# print(points)