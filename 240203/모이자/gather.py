import sys

n = int(input())
homes = list(map(int, input().split()))
min_dis = sys.maxsize
for i in range(n) :
    sub_dis = 0
    for j in range(n) :
        sub_dis += abs(j-i) * homes[j]
    min_dis = min(min_dis, sub_dis)

print(min_dis)