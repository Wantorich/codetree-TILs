MAX_IDX = 1000
rects = [
    list(map(lambda x : x + MAX_IDX,tuple(map(int, input().split()))))
    for _ in range(3)
]

# print(rects)

coord = [[0 for _ in range(2*MAX_IDX+1)] for _ in range(2*MAX_IDX+1)]
for i, rect in enumerate(rects) :
    x1, y1, x2, y2 = rect
    for row in range(y1, y2) :
        for col in range(x1, x2) :
            if i == 2 :
                coord[row][col] = 0
            else :
                coord[row][col] = 1


cnt = 0
for row in coord :
    cnt += sum(row)

print(cnt)