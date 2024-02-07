ability = list(map(int, input().split()))

def get_diff(i, j, k) :
    sum1 = ability[i] + ability[j] + ability[k]
    sum2 = sum(ability) - sum1
    return abs(sum1 - sum2)

min_diff = 10000
n = len(ability)
for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            min_diff = min(min_diff, get_diff(i,j,k))
        
print(min_diff)