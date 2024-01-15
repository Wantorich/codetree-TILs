cnt = 0
hospital = [0] * 5
for _ in range(3) :
    status, degree = input().split()
    if status == 'Y' :
        if int(degree) >= 37 :
            hospital[1] += 1
            cnt += 1
        else :
            hospital[3] += 1
    else :
        if int(degree) >= 37 :
            hospital[2] += 1
        else :
            hospital[4] += 1

for i in range(1, 5) :
    print(hospital[i], end=' ')

if cnt >= 2 :
    print('E')