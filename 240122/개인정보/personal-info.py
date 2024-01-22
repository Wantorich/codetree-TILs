people = [input().split() for _ in range(5)]

people.sort(key=lambda x : x[0])
print('name')
for n, h, w in people :
    print(n, h, w)

print()

people.sort(key=lambda x : -int(x[1]))
print('height')
for n, h, w in people :
    print(n, h, w)