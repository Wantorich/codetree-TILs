MAX = 1000 * 1000

n, m = map(int, input().split())
pos_a, pos_b = [0] * (MAX + 1), [0] * (MAX + 1)

idx_a = 1
for _ in range(n) :
    v, t = map(int, input().split())
    while t > 0 :
        pos_a[idx_a] = pos_a[idx_a-1] + v
        idx_a += 1 
        t -= 1

idx_b = 1
for _ in range(m) :
    v, t = map(int, input().split())
    while t > 0 :
        pos_b[idx_b] = pos_b[idx_b-1] + v
        idx_b += 1 
        t -= 1

# 전거랑 현재거를 비교해야하고 일단
# 0 0 이 아닌데 0이 되면 바뀐거지
# 곱해서 음수가 되도 바뀐거고

changed = 0
heading = [0] * idx_a
for i in range(1, idx_a) :
    heading[i] = 0 if pos_a[i] >= pos_b[i] else 1

for i in range(2, len(heading)) :
    if heading[i] + heading[i-1] == 1 :
        changed += 1

print(changed)