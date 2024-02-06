n, m = map(int, input().split())
nums = list(map(int, input().split()))
targets = list(map(int, input().split()))

targets.sort()
sub_arr = []
cnt = 0

for i in range(n - m + 1) :
    for j in range(i, i+m) :
        sub_arr.append(nums[j])
    sub_arr.sort()
    if sub_arr == targets :
        cnt += 1
    sub_arr.clear()

print(cnt)