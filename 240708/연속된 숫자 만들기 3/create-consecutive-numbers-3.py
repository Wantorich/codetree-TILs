a, b, c = tuple(map(int, input().split()))

cnt = 0
while not ((a+1 == b) and (b+1 == c)):
    if b-a < c-b:
        t = b+1
        a = b
        b = t
    else:
        t = b-1
        c = b
        b = t
    cnt += 1

print(cnt)