n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(n) :
    for j in range(i, n) :
        average = sum(nums[i:j+1]) / (j+1 - i)
        for k in range(i, j+1) :
            if nums[k] == average :
                cnt += 1
                break
print(cnt)