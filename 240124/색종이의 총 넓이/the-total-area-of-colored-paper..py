n = int(input())
MAX_IDX = 100
rects = [
    list(map(lambda x : x + MAX_IDX,tuple(map(int, input().split()))))
    for _ in range(n)
]

coord = [[0 for _ in range(2*MAX_IDX+1)] for _ in range(2*MAX_IDX+1)]
for rect in rects :
    x1, y1 = rect
    for row in range(y1, y1+8) :
        for col in range(x1, x1+8) :
            coord[row][col] = 1


cnt = 0
for row in coord :
    cnt += sum(row)

print(cnt)