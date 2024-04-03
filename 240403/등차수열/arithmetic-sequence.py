n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
for k in range(min(nums), max(nums)) :
    cnt = 0
    for i in range(len(nums)) :
        for j in range(i+1, len(nums)) :
            if abs(nums[i]-k) == abs(nums[j]-k) :
                cnt += 1
    ans = max(ans, cnt)
print(ans)