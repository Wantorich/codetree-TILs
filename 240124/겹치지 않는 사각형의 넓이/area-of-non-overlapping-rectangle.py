MAX_IDX = 1000
rects = [
    list(map(lambda x : x + MAX_IDX,tuple(map(int, input().split()))))
    for _ in range(3)
]

min_idx = MAX_IDX
max_idx = -1000 

coord = [[0 for _ in range(2*MAX_IDX+1)] for _ in range(2*MAX_IDX+1)]
for i, rect in enumerate(rects) :
    x1, y1, x2, y2 = rect
    min_idx = y1 if y1 < min_idx else min_idx
    max_idx = y2 if y2 > max_idx else max_idx
    for row in range(y1, y2) :
        for col in range(x1, x2) :
            if i == 2 :
                coord[row][col] = 0
            else :
                coord[row][col] = 1


cnt = 0
for row in coord[min_idx:max_idx+1] :
    cnt += sum(row)

print(cnt)