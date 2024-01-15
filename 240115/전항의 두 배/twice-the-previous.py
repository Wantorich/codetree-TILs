a, b = map(int, input().split())
cnt = 2
print(a,b, end=' ')
while cnt < 10 :
    n = 2*a + b
    print(n, end=' ')
    a = b
    b = n
    cnt += 1