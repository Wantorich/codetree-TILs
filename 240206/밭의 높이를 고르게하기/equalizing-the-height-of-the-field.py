n, h, t = map(int, input().split())
nums = list(map(int, input().split()))

min_time = 100
for i in range(n - t + 1) :
    sub_sum = 0
    for j in range(i, i+3) :
        sub_sum += abs(nums[j] - h)
    min_time = min(min_time, sub_sum)

print(min_time)