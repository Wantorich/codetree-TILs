import sys

ability = list(map(int, input().split()))
n = len(ability)

min_diff = sys.maxsize
for i in range(n) :
    for j in range(i+1, n) :
        sum1 = ability[i] + ability[j]
        for k in range(n) :
            for l in range(k+1, n) :
                if k != i and k != j and l != i and l != j :
                    sum2 = ability[k] + ability[l]
                    sum3 = sum(ability) - (sum1 + sum2)
                    new_list = [sum1, sum2, sum3]
                    min_diff = min(min_diff, max(new_list) - min(new_list))


print(min_diff)