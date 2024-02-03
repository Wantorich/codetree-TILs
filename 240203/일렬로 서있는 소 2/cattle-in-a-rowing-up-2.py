n = int(input())
cows = list(map(int, input().split()))
cnt = 0
for i in range(n) :
    first = cows[i]
    for j in range(i+1, n) :
        second = cows[j]
        if second >= first :
            for k in range(j+1, n) :
                third = cows[k]
                if third >= second :
                    cnt += 1

print(cnt)