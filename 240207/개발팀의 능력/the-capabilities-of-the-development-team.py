import sys

abil = list(map(int, input().split()))
n = len(abil)
min_diff = sys.maxsize
exist = False

for i in range(n) :
    for j in range(i+1, n) :
        sum1 = abil[i] + abil[j]
        for k in range(n) :
            if k == i or k == j or abil[k] == sum1:
                continue
            sum2 = abil[k]
            sum3 = sum(abil) - (sum1 + sum2)
            if sum3 != sum1 and sum3 != sum2 :
                new_list = [sum1, sum2, sum3]
                min_diff = min(min_diff, max(new_list) - min(new_list))
                exist = True

if exist :
    print(min_diff)
else :
    print(-1)