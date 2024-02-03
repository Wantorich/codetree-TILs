import sys

def calculate_dist(tuple_a, tuple_b) :
    x1, y1 = tuple_a
    x2, y2 = tuple_b
    return abs(x1-x2) + abs(y1-y2)

n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]
min_dist = sys.maxsize

for i in range(1, n-1) :
    pop_checks = checkpoints[:i] + checkpoints[i+1:]
    dist = 0
    for j in range(n-2) :
        dist += calculate_dist(pop_checks[j], pop_checks[j+1])
    min_dist = min(min_dist, dist)

print(min_dist)