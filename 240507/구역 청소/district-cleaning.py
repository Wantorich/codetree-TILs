# 각 구한 더하고 겹치는 구간 빼면 총 구간
a, b = map(int, input().split())
c, d = map(int, input().split())

sum_dis = (b-a) + (d-c)

if c <= b <= d :
    if c <= a :
        sum_dis -= b-a
    else :
        sum_dis -= b-c
elif a <= d <= b :
    if a <= c :
        sum_dis -= d-c
    else :
        sum_dis -= d-a
        

print(sum_dis)