import sys

n = int(input())
arr = list(map(int, input().split()))
max_val = arr[0]
idx = -1
for num in arr[1:] :
    if num >= max_val :
        max_val = num
        idx = arr.index(num)


max_left = -sys.maxsize
for num in arr[:idx] :
    if idx <= 0 :
        break;
    if max_left <= num :
        max_left = num

max_right = -sys.maxsize
for num in arr[idx+1:] :
    if max_right <= num :
        max_right = num

print(max_left, max_right)
print(max_val, end=' ')
print('%d' % max_left if max_left >= max_right else max_right)