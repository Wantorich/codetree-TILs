n = int(input())
for i in range(1, n+1) :
    sum_ = 0
    if i > 10 :
        sum_ = (i // 10) + (i % 10)
    else :
        sum_ = i
    if i % 3 == 0 or sum_ % 3 == 0 :
        print(0, end=' ')
    else :
        print(i, end=' ')