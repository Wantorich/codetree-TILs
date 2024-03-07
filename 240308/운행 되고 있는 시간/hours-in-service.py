import sys

n = int(input())
workers = [tuple(map(int, input().split())) for _ in range(n)]
max_eff = -sys.maxsize

for i in range(n) :
    table = [0] * 1000
    for j in range(n) :
        if i == j :
            continue
        start, end = workers[j]
        for k in range(start, end) :
            table[k] = 1
    max_eff = max(max_eff, sum(table))

print(max_eff)