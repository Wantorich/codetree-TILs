n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
idx = -1
for i, num in enumerate(arr) :
    if num > max_val :
        max_val = num
        idx = i

max_left = max(arr[:idx])
max_right = max(arr[idx+1:])
max_sec = max_left if max_left >= max_right else max_right
print(max_val, max_sec)