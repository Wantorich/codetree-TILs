n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum_val = sum(nums)
ans = sum_val

for val in range(1, sum_val+1) : # 최소값이 val
    part_sum = 0
    sep = m-1
    flag = True
    for num in nums :
        part_sum += num
        if part_sum <= val :
            continue
        else :
            if num > val :
                flag = False
                break
            if sep > 0 :
                sep -= 1
                part_sum = num
            else :
                flag = False
                break
    if flag :
        print(val)
        break