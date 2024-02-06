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
        g_count = sliced.count('G')
        h_count = sliced.count('H')
        if g_count == h_count or len(sliced) == g_count or len(sliced) == h_count :
            max_len = max(max_len, j-i)

print(max_len)