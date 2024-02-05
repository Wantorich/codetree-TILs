n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y) :
    return 0 <= x < n and 0 <= y < n

def num_of_1(x,y) :
    if y+2 > n-1 :
        return 0
    cnt = 0
    for k in range(y, y+3) :
        if grid[x][k] == 1 :
            cnt += 1
    return cnt

max_cnt = 0
for i in range(n) :
    for j in range(n) :
        for k in range(i, n) :
            for l in range(j, n) :
                if i == k and l < j+3 :
                    continue
                max_cnt = max(max_cnt, num_of_1(i, j) + num_of_1(k, l))

print(max_cnt)