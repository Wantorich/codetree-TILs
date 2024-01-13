flag = True
for _ in range(5) :
    n = int(input())
    if n % 3 != 0 :
        flag = False
        break
print('%d' % 1 if flag else 0)