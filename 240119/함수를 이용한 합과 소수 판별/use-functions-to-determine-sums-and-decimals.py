a, b = map(int, input().split())

def is_prime(n) :
    for i in range(2, n) :
        if n % i == 0 :
            return False
    return True

def is_sum_even(n) :
    sum_val = 0
    while n > 0 :
        remain = n % 10
        sum_val += remain
        n //= 10

    if sum_val % 2 == 0 :
        return True
    else :
        return False

cnt = 0
for i in range(a, b+1) :
    if is_prime(i) and is_sum_even(i) :
        cnt += 1
print(cnt)