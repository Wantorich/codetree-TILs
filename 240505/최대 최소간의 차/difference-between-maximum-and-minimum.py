n, k = map(int, input().split())
nums = list(map(int, input().split()))

diff = max(nums) - min(nums)
cost = 0
idx = 0

while max(nums) - min(nums) > k :
    n = nums[idx]
    if n == max(nums) :
        nums[idx] -= 1
        cost += 1
    elif n == min(nums) :
        nums[idx] += 1
        cost += 1
    idx = (idx+1) % n

print(cost)