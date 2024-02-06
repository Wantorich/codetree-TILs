MAX_NUM = 100
n, k = map(int, input().split())
places = [0] * (MAX_NUM + 1)

for _ in range(n) :
    candy, idx = map(int, input().split())
    places[idx] += candy

max_val = 0
# k <= c , c+k <= MAX_NUM
for c in range(k, MAX_NUM - k + 1) :
    sub_sum = 0
    for j in range(c-k, c+k+1) :
        sub_sum += places[j]
    max_val = max(max_val, sub_sum)

print(max_val)