n, m = map(int, input().split())
list_ = list(map(int, input().split()))
sum_ = 0
while m >= 1 :
    sum_ += list_[m-1]
    if m % 2 == 1 :
        m -= 1
    else :
        m //= 2
print(sum_)