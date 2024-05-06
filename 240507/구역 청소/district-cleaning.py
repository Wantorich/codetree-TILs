# 각 구한 더하고 겹치는 구간 빼면 총 구간
a, b = map(int, input().split())
c, d = map(int, input().split())

sum_dis = (b-a) + (d-c)

if c <= b <= d :
    sum_dis -= b-c
elif a <= d <= b :
    sum_dis -= d-a

print(sum_dis)