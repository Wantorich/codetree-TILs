MAX_IDX = 100
n = int(input())
place = [0] * (2*MAX_IDX+1)

for _ in range(n) :
    a, b = map(int, input().split())
    for i in range(a, b) :
        place[i] += 1

print(max(place))