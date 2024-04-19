n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

for i in range(1, n) :
    if nums[i] - nums[0] <= k :
        continue
    print(i)
    break