n, budget = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(n)]

# 가격 리스트를 만들어야함
price_list = []
for i in range(n) :
    price_temp = []
    for j in range(n) :
        price, ship = data[j][0], data[j][1]
        if j == i :
            price //= 2
        price_temp.append(price+ship)
    price_temp.sort()
    price_list.append(price_temp)

max_pay = 0
for i in range(n) :
    curr_price = price_list[i]
    pay = budget
    cnt = 0
    for j in range(n) :
        p = curr_price[j]
        if i == j :
            p //= 2
        pay -= p
        if pay < 0 :
            break
        cnt += 1
    max_pay = max(max_pay, cnt)

print(max_pay)