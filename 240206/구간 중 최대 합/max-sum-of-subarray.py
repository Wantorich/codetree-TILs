n, k = map(int, input().split())
nums = list(map(int, input().split()))
max_val = 0
for i in range(n - k + 1) :
    sum_val = 0
    for j in range(i, i+k) :
        sum_val += nums[j]
    max_val = max(max_val, sum_val)

print(max_val)