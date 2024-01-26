n = int(input())
cnt = 1
max_cnt = cnt
prev = int(input())
while n > 1 :
    num = int(input())
    if num != prev :
        cnt = 1
        prev = num
    else :
        cnt += 1
    if max_cnt < cnt :
        max_cnt = cnt
    n -= 1

print(max_cnt)