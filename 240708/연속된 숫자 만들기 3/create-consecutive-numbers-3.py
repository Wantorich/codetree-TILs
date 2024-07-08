a, b, c = tuple(map(int, input().split()))

if a+1 == b and b+1 == c:
    print(0)
elif a+1 == b:
    print(c-b-1)
elif b+1 == c:
    print(b-1-a)
else:
    if b-a < c-b:
        t = b+1
        print(c-t)
    else:
        t = b-1
        print(t-a)




# 한번 a, a+1, b의 구조가 형성이 되면
# 3 4 20되면 5~19까지 15번 c - b - 1 횟수