n = int(input())
people = [input().split() for _ in range(n)]

people.sort(key=lambda x : (int(x[1]), -int(x[2])))
for n, h, w in people :
    print(n, h, w)