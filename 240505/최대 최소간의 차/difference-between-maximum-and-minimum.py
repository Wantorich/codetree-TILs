n, k = map(int, input().split())
nums = list(map(int, input().split()))

cost = 0
idx = 0

while max(nums) - min(nums) > k :
    num = nums[idx]
    if num == max(nums) :
        nums[idx] -= 1
        cost += 1
    elif num == min(nums) :
        nums[idx] += 1
        cost += 1
    idx = (idx+1) % n # 0 1 2 3 .. n-1 n->0

print(cost)