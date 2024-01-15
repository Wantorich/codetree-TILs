n = int(input())
arr = list(map(int, input().split()))
res = 0

for i in range(n-1) :
    sub_max = 0
    for j in range(i+1, n) :
        sub_profit = arr[j] - arr[i]
        if sub_max <= sub_profit :
            sub_max = sub_profit
    if sub_max >= res :
        res = sub_max

print(res)