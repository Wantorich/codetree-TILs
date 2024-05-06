import sys

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
ans = 'No'

for i in range(n) : # 하나씩 제외
    max_x1 = 0
    min_x2 = sys.maxsize
    for j in range(n) :
        if i == j :
            continue
        x1, x2 = lines[j]
        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)
    if max_x1 <= min_x2 :
        ans = 'Yes'
        break

print(ans)