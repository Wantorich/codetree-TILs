n = int(input())
heights = [int(input()) for _ in range(n)]
ans = 0
for i in range(max(heights)) :
    temp = [height - i for height in heights]
    cnt = 0
    for j in range(n) :
        if temp[j] > 0 :
            cnt += 1
            if j+1 < n and temp[j+1] > 0 :
                cnt -= 1
    ans = max(ans, cnt)

print(ans)