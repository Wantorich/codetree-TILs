mid, final = map(int, input().split())
money = 0
if mid >= 90 :
    if final >= 95 :
        money += 100000
    elif final >= 90 :
        money += 50000
print(money)