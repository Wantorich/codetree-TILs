arr = list(map(int, input().split()))
min_val = 1
max_val = 1000

for num in arr[1:] :
    if num > 500 :
        if max_val >= num :
            max_val = num
    else :
        if min_val <= num :
            min_val = num
print(min_val, max_val)