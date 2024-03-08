import sys

n, budget = map(int, input().split())
price = [int(input()) for _ in range(n)]

min_pay = n
for i in range(n) :
    pay = budget
    for j in range(n) :
        p = price[j]
        if i == j :
            p //= 2
        pay -= p
        if pay < 0 :
            break
    min_pay = min(min_pay, j+1)

print(min_pay)