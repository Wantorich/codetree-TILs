def possible(num) :
    arr = []
    for i, v in enumerate(nums) :
        if v < num :
            arr.append(i) # index array

    for i in range(len(arr)-1) :
        if arr[i+1] - arr[i] > k :
            return False
    return True

n, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = max(nums)
for i in range(ans, max(nums[0], nums[-1]), -1) :
    if possible(i) :
        ans = min(ans, i-1)

print(ans)