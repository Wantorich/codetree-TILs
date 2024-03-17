X, Y = map(int, input().split())

def digit_sum(n) :
    if n < 10 :
        return n
    else :
        return digit_sum(n // 10) + (n % 10)

ans = 0
for n in range(X, Y+1) :
    # 각 자리수의 합을 계산, 단 몇자리인지는 모름
    # num_list = []
    # while n > 0 :
    #     num_list.append(n%10)
    #     n //= 10
    ans = max(ans, digit_sum(n))

print(ans)