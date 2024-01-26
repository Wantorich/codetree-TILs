n, t = map(int, (input().split()))
arr = list(map(int, (input().split())))
cnt = max_cnt = 0
arr = list(filter(lambda x : x > t, arr))
for i in range(len(arr)) :
    if i == 0 or arr[i-1] < arr[i] :
        cnt += 1
    else :
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)