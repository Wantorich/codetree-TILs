import sys

n, budget = map(int, input().split())
price = [int(input()) for _ in range(n)]
price.sort()

max_pay = 0
for i in range(n) :
    pay = budget
    for j in range(n) :
        p = price[j]
        if i == j :
            p //= 2
        pay -= p
        if pay <= 0 :
            break
    max_pay = max(max_pay, j)

print(max_pay)