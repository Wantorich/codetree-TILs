n = int(input())

for _ in range(n) :
    m = int(input())
    cnt = 0
    while m > 1 :
        if m % 2 == 0 :
            m //= 2
        else :
            m = 3*m + 1
        cnt += 1
    print(cnt)