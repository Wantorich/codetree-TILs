import sys

n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 2개를 제외하고 나올수 있는 합을 모두 구하고
# 그 중에 S와 가장 가까운값 찾기

sum_s = sum(nums)
add_val = 0
diff_min = sys.maxsize
for i in range(n) :
    for j in range(i+1, n) :
        add_val = nums[i] + nums[j]
        sub_val = sum_s - add_val
        diff_min = min(diff_min, abs(s - sub_val))

print(diff_min)