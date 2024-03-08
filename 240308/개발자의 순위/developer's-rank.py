k, n = map(int, input().split())
data_set = [list(map(int, input().split())) for _ in range(k)]
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(k) :
    data = data_set[i]
    for j in range(n) :
        for k in range(j+1, n) :
            grid[data[j]][data[k]] += 1

ans = 0
for i in range(n+1) :
    ans += grid[i].count(k)

print(ans)