n, t = map(int, (input().split()))
arr = list(map(int, (input().split())))
cnt = max_cnt = 0
for i in range(n) :
    if i == 0 or (arr[i-1] < arr[i] and t < arr[i-1] and t < arr[i]) :
        cnt += 1
    else :
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)