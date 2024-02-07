n = int(input())
nums, cnt1, cnt2 = [0] * n, [0] * n, [0] * n

for i in range(n) :
    nums[i], cnt1[i], cnt2[i] = map(int, input().split())

def incr_cnt1(arr, num) :
    cnt = 0
    for i in range(3) :
        if arr[3-(i+1)] == num % 10 :
            cnt += 1
        num //= 10
    return cnt

def incr_cnt2(arr, num) :
    cnt = 0
    num_list = list(map(int, list(str(num))))
    for i in range(3) :
        if arr[i] != num_list[i] and arr[i] in num_list :
            cnt += 1
    return cnt
    
cnt = 0
for i in range(1, 10) :
    for j in range(1, 10) :
        for k in range(1, 10) :
            if i == j or j == k or i == k :
                continue
            arr = [i, j, k]
            flag = True
            for l in range(n) :
                if incr_cnt1(arr, nums[l]) != cnt1[l] or incr_cnt2(arr, nums[l]) != cnt2[l]:
                    flag = False
                    break
            if flag :
                cnt += 1
                
print(cnt)