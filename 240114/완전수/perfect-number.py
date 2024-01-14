a, b = map(int, input().split())
cnt = 0
for num in range(a, b+1) :
    sum_ = 0
    for i in range(1, num) :
        if num % i == 0 :
            sum_ += i
    if sum_ == num :
        cnt += 1
print(cnt)