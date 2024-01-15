n = int(input())
arr = list(map(int, input().split()))
res = -1
max_val = arr[0]
for num in arr[1:] :
    if num >= max_val :
        max_val = num

cnt_arr = [0] * (max_val + 1)
for num in arr :
    cnt_arr[num] += 1

for i, v in enumerate(cnt_arr) :
    if v == 1 and i >= res :
        res = i

print(res)