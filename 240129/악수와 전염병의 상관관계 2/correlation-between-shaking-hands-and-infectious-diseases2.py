n, k, p, t = map(int, input().split())
coders = [0] * (n+1)
coders[p] = 1

info_arr = [tuple(map(int, input().split())) for _ in range(t)]
info_arr.sort(key = lambda x : x[0])

for info in info_arr[:k] :
    _, x, y = info
    if coders[x] == 1 or coders[y] == 1 :
        coders[x] = 1
        coders[y] = 1

print(''.join(map(str, coders[1:])))