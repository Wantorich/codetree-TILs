n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
max_idx = n+1
while max_idx > 1 :
    max_val = 0
    for i, num in enumerate(arr[:max_idx]) :
        if max_val < num :
            max_val = num
            max_idx = i
    print(max_idx, end=' ')