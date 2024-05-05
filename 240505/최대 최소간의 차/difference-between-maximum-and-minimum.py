n, k = map(int, input().split())
nums = list(map(int, input().split()))

cost = 0
idx = 0
diff = max(nums) - min(nums)
while diff > k :
    max_val = max(nums)
    min_val = min(nums)
    min_idx = []
    max_idx = []
    for i in range(n) :
        if nums[i] == max_val :
            max_idx.append(i)
        elif nums[i] == min_val :
            min_idx.append(i)
    
    if len(max_idx) < len(min_idx) :
        for index in max_idx :
            nums[index] -= 1
            cost += 1
    else :
        for index in min_idx :
            nums[index] += 1
            cost += 1
    diff = max(nums) - min(nums)

print(cost)