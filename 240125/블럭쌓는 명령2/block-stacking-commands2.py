n, k = map(int, input().split())
place = [0] * (n+1)

for _ in range(k) :
    a, b = map(int, input().split())
    for i in range(a, b+1) :
        place[i] += 1

print(max(place))