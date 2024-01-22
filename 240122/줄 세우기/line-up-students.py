n = int(input())
# people = [
#     tuple(map(int, input().split()))
#     for i in range(1, n+1)
# ]

people = []
for i in range(1, n+1) :
    h, w = map(int, input().split())
    people.append((h, w, i))

people.sort(key=lambda x : (-x[0], -x[1], x[2]))

for h, w, i in people :
    print(h, w, i)