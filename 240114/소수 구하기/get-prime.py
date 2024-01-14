n = int(input())

for num in range(2, n+1) :
    flag = True
    for i in range(2, num) :
        if num % i == 0 :
            flag = False
            break
    if flag :
        print(num, end=' ')