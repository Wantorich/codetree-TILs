n = int(input())
people = [
    tuple(input().split())
    for _ in range(n)
]
people.sort(key=lambda x : (-int(x[1]), -int(x[2]), -int(x[3])))

for name, kor, eng, math in people :
    print(name, kor, eng, math)