X, Y = map(int, input().split())

def find_num(n) :
    str_nums = list(map(int, list(str(n))))
    # str_nums.sort()
    # fst_ = str_nums[0]
    # last_ = str_nums[-1]
    fst_ = min(str_nums)
    last_ = max(str_nums)
    fst_cnt = last_cnt = 0
    for num in str_nums :
        if fst_ != num :
            fst_cnt += 1
        if last_ != num :
            last_cnt += 1
    
    if fst_cnt == 1 or last_cnt == 1 :
        return True
    else :
        return False

ans = 0
for i in range(X, Y+1) :
    if find_num(i) :
        ans += 1
print(ans)