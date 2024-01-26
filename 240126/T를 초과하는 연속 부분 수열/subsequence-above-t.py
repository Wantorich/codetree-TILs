n, t = map(int, (input().split()))
arr = list(map(int, (input().split())))
cnt = max_cnt = 0
for i in range(n) :
    if i == 0 :
        if arr[i] > t :
            cnt = 1
    elif arr[i] > t :
        if arr[i-1] > t and arr[i-1] < arr[i] :
            cnt += 1
        else :
            cnt = 1
    else :
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)