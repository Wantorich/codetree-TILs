import sys

n = int(input())
people = [int(input()) for _ in range(n)]
dist_min = sys.maxsize
for room in range(n) :
    dist_sum = 0
    for j in range(n) :
        dist_sum += ((j- room + n) % n) * people[j]
    dist_min = min(dist_min, dist_sum)

print(dist_min)