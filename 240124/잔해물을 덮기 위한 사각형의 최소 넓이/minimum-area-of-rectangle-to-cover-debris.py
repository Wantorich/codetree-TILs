MAX_IDX = 1000
rects = [
    list(map(lambda x : x + MAX_IDX,tuple(map(int, input().split()))))
    for _ in range(2)
]

coord = [[0 for _ in range(2*MAX_IDX+1)] for _ in range(2*MAX_IDX+1)]
for i, rect in enumerate(rects) :
    x1, y1, x2, y2 = rect
    for row in range(y1, y2) :
        for col in range(x1, x2) :
            if i == 0 :
                coord[row][col] = 1
            else :
                coord[row][col] = 0




cnt = 0
max_row = max_col = 0
for row in coord :
    this_row = sum(row)
    if this_row > 0 :
        max_row += 1
        max_col = this_row if this_row > max_col else max_col

print(max_row * max_col)