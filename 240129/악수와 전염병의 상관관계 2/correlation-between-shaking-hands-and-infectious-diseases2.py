n, k, p, t = map(int, input().split())
coders, count = [0] * (n+1), [0] * (n+1)
coders[p] = 1
count[p] = k

info_arr = [tuple(map(int, input().split())) for _ in range(t)]
info_arr.sort(key = lambda x : x[0])

for info in info_arr :
    _, x, y = info
    if coders[x] != 1 and coders[y] != 1 :
        continue
    elif coders[x] == 1 and coders[y] != 1 :
        if count[x] <= 0 :
            continue
        count[x] -= 1
        coders[y] = 1
        count[y] = k
    elif coders[x] != 1 and coders[y] == 1 :
        if count[y] <= 0 :
            continue
        count[y] -= 1
        coders[x] = 1
        count[x] = k
    else :
        count[x] -= 1
        count[y] -= 1

print(''.join(map(str, coders[1:])))