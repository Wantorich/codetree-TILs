n, m = map(int, input().split())

mov_a = []
for _ in range(n) :
    v, t = map(int, input().split())
    while t > 0 :
        mov_a.append(v)
        t -= 1

mov_b = []
for _ in range(m) :
    v, t = map(int, input().split())
    while t > 0 :
        mov_b.append(v)
        t -= 1

dis_a = [0] * len(mov_a)
dis_b = [0] * len(mov_a)
winner = False
cnt = 0
for i in range(len(mov_a)) :
    dis_a[i] = sum(mov_a[:i+1])
    dis_b[i] = sum(mov_b[:i+1])
    if dis_a[i] > dis_b[i] :
        if winner == 'right' :
            cnt += 1
        winner = 'left'
    else :
        if winner == 'left' :
            cnt += 1
        winner = 'right'

print(cnt)