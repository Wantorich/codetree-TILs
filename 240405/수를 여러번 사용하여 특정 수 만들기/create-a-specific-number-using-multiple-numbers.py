a, b, c = map(int, input().split())
ans = 0
for i in range (c // a) :
    for j in range(b // a) :
        max_num = a * (i + 1) + b * (j + 1)
        if max_num <= c :
            ans = max(ans, max_num)

print(ans)