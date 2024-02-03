n = int(input())
nums = list(map(int, input().split()))
max_val = -1
for i in range(n-2) :
    for j in range(i+2, n) :
        sub_max = nums[i] + nums[j]
        max_val = max(max_val, sub_max)

print(max_val)