n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum_val = sum(nums)
ans = sum_val

for val in range(1, sum_val+1) :
    part_sum = 0
    # max_sum = 0
    sep = m-1
    flag = True
    for num in nums :
        if part_sum + num > val :
            if sep > 0 :
                # max_sum = max(max_sum, part_sum)
                part_sum = num
                sep -= 1
            else :
                flag = False
                break    
        else :
            part_sum += num
    if flag :
        print(val)
        break