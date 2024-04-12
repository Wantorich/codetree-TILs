n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

for i in range(n) :
    sum_val = 0
    for j in range(m) :
        sum_val += nums[i]
        i = nums[i] - 1
    ans = max(ans, sum_val)

print(ans)