n = int(input())
for i in range(1, n+1) :
    head = -1
    if i > 10 :
        head = i // 10
    tail = i % 10
    if i % 3 == 0 or head % 3 == 0 or tail % 3 == 0:
        print(0, end=' ')
    else :
        print(i, end=' ')