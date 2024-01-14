a, b = map(int, input().split())
cnt = 0
for num in range(a, b+1) :
    sub_cnt = 0
    for i in range(1, num+1) :
        if num % 1 == 0 :
            sub_cnt += 1
    if sub_cnt == 3 :
        cnt += 1
print(cnt)