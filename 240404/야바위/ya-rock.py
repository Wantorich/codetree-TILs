n = int(input())
step = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(1, n+1) :
    cups = [0] * (n+1)
    cups[i] = 1
    cnt = 0
    for (a, b, c) in step : 
        cups[a], cups[b] = cups[b], cups[a]
        if cups[c] == 1 :
            cnt += 1
    ans = max(ans, cnt)

print(ans)