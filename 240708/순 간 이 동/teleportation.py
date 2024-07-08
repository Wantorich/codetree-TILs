A, B, x, y = tuple(map(int, input().split()))

m1 = abs(A-B)
m2 = abs(A-x) + abs(B-y)
m3 = abs(A-y) + abs(B-x)

print(min(m1, m2, m3))