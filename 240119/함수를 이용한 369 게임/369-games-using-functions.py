a, b = map(int, input().split())

def is_3_mulitple(n) :
    str_num = str(n)
    for s in str_num :
        num = int(s)
        if num % 3 == 0 and num != 0:
            return True
    return False

def is_magic_num(n) :
    # 3, 6, 9 중 하나가 들어가있거나 
    # 즉 모두 안들어있는경우를 전체에서 뺌 
    if n % 3 == 0 :
        return True
    else :
        if is_3_mulitple(n) :
            return True
        # if n >= 10 : 
        #     divisor = n // 10
        #     remain = n % 10
        #     if (divisor % 3 == 0) or (remain % 3 == 0) :
        #         return True
        # else :
        #     if n % 3 == 0 :
        #         return True
    return False
        


cnt = 0
for i in range(a, b+1) :
    if is_magic_num(i) :
        cnt += 1
print(cnt)