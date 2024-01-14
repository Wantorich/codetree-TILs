n = int(input())
sum_ = 0
for i in range(1, n) :
    if n % i == 0 :
        sum_ += i
print('%c' % 'P' if sum_ == n else 'N')