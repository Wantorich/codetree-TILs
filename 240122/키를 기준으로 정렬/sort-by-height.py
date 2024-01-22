n = int(input())
people = [
    tuple(input().split())
    for _ in range(n)
]
people.sort(key=lambda x : x[1])

for name, height, weight in people :
    print(name, height, weight)