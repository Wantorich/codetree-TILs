def record(array, command) :
    for com in command :
        dis, direct = com
        dis = int(dis)
        while dis > 0 :
            if direct == 'R' :
                array.append(array[len(array)-1] + 1)
            else :
                array.append(array[len(array)-1] - 1)
            dis -= 1


n, m = map(int, input().split())
com_a = [input().split() for _ in range(n)]
com_b = [input().split() for _ in range(m)]

record_a = [0]
record_b = [0]

record(record_a, com_a)
record(record_b, com_b)

last_pos = -1
cnt = 0
flag = -1
if len(record_a) >= len(record_b) :
    longer = len(record_a)
    shorter = len(record_b)
    flag = 'left'
else :
    longer = len(record_b)
    shorter = len(record_a)
    flag = 'right'

for i in range(1, shorter) :
    if record_a[i] == record_b[i] and record_a[i-1] != record_b[i-1]:
        cnt += 1
    if flag == 'left' :
        last_pos = record_b[i]
    else :
        last_pos = record_a[i]

for i in range(shorter, longer-1) :
    if flag == 'left' :
        if record_a[i] == last_pos and record_a[i-1] != last_pos:
            cnt += 1
    else :
        if record_b[i] == last_pos and record_b[i-1] != last_pos:
            cnt += 1

print(cnt)