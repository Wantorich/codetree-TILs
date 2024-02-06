n = int(input())
MAX_NUM = 100
max_len = 0
arr = [0] * (MAX_NUM + 1)

for i in range(n) :
    index, photo = input().split()
    arr[int(index)] = photo

for i in range(MAX_NUM+1) :
    for j in range(i, MAX_NUM+1) :
        if arr[i] == 0 :
            break
        if arr[j] == 0 :
            continue
        sliced = arr[i:j+1]
        if len(sliced) % 2 == 0 and sliced.count('G') == sliced.count('H') :
            max_len = max(max_len, j-i)
        elif len(sliced) == sliced.count('G') or len(sliced) == sliced.count('H') :
            max_len = max(max_len, j-i)

print(max_len)