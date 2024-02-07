n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# n까지 있으면 n-1(0) n(1) 1 2 3 -> 차가 n-2보다 크거나 같고 2보다 작거나 같음

def is_match(x, y, z, a, b, c) :
    diff1 = abs(a - x)
    diff2 = abs(b - y)
    diff3 = abs(c - z)
    if 2 < diff1 < n-2 or 2 < diff2 < n-2 or 2 < diff3 < n-2 :
        return False
    return True

cnt = 0
for i in range(1, n+1) :
    for j in range(1, n+1) :
        for k in range(1, n+1) :
            if is_match(i, j, k, a1, b1, c1) or is_match(i, j, k, a2, b2, c2) :
                cnt += 1

print(cnt)