# a b c d e
# ab bc cd de
# 30 - 23 = 7 , a + e = 7
# 2 2 3 4 2 5

n = int(input())
nums = list(map(int, input().split()))

sum_val = 0
cnt = 1
while (cnt <= n) :
    sum_val += cnt
    cnt += 1

remain = 2*sum_val - sum(nums)

for i in range(1, remain) :
    if i > n or remain - i > n :
        continue
    temp = {i}
    # print(temp)
    k = i
    for j in range(len(nums)) :
        diff = nums[j] - k
        if diff <= n :
            k = diff
            temp.add(k)
    temp.add(remain-i)
    # print(temp)
    if len(temp) == n :
        for n in temp :
            print(n, end=' ')
        break