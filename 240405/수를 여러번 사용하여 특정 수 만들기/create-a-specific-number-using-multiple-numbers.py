a, b, c = map(int, input().split())
ans = 0

for i in range (c // a + 1) :
    for j in range(c // b + 1) :
        max_num = a * i + b * j
        if max_num <= c :
            ans = max(ans, max_num)

print(ans)