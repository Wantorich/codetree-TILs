import sys

n = int(input())
MAX_IDX = 100
# coord = [[0] * (MAX_IDX+1) for _ in range(MAX_IDX+1)]
# for i in range(n) :
#     x, y = map(int, input().split())
#     coord[x][y] = 1
points = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize

for x_line in range(1, MAX_IDX+1) :
    for y_line in range(1, MAX_IDX+1) :
        places = [0 for _ in range(5)]
        for x, y in points :
            if x < x_line :
                if y < y_line :
                    places[3] += 1
                else :
                    places[2] += 1
            else :
                if y < y_line :
                    places[4] += 1
                else :
                    places[1] += 1
        ans = min(max(places), ans)

print(ans)