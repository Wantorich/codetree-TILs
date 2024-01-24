n = int(input())
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

coord = [[0 for _ in range(201)] for _ in range(201)]
for rect in rects :
    rect = list(map(lambda x : x + 100, rect))
    x1, y1, x2, y2 = rect
    for row in range(y1, y2) :
        for col in range(x1, x2) :
            coord[row][col] = 1

cnt = 0
for row in coord :
    cnt += sum(row)

print(cnt)