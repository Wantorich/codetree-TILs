MAX_NUM = 100
n, k = map(int, input().split())
places = [0] * (MAX_NUM + 1)

for _ in range(n) :
    candy, idx = map(int, input().split())
    places[idx] += candy

max_val = 0
# k <= c , c+k <= MAX_NUM
for c in range(k, k + MAX_NUM) :
    sub_sum = 0
    for i in range(c-k, min(c+k+1, MAX_NUM+1)) :
        sub_sum += places[i]
    max_val = max(max_val, sub_sum)

print(max_val)