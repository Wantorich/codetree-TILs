n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
ans = 0

for i in range(1, n) :
    slice_arr = nums[i:]
    min_val = min(slice_arr)
    cnt = 0
    for n in slice_arr :
        if n - min_val <= k :
            cnt += 1
    ans = max(ans, cnt)

print(ans)