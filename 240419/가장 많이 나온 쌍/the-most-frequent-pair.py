n, m = map(int,input().split())
tuples = [tuple(map(int, input().split())) for _ in range(m)]
ans = 0

for (x,y) in tuples :
    cnt = 0 
    for (a, b) in tuples :
        if (x, y) == (a, b) or (x, y) == (b, a) :
            cnt += 1
    ans = max(ans, cnt)

print(ans)