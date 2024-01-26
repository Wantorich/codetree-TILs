n = int(input())
cnt = 1
prev = int(input())
while n > 1 :
    num = int(input())
    if num != prev :
        cnt += 1
        prev = num
    n -= 1

print(cnt)