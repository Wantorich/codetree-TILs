def erase(x1, x2, arr) :
    for k in range(x1, x2+1) :
        arr[k] -= 1

MAX_NUM = 100
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
array = [0] * (MAX_NUM+1)
for i in range(n) :
    x1, x2 = lines[i]
    for k in range(x1, x2+1) :
        array[k] += 1

ans = 0

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            copy = array[:]
            flag = True
            erase(*lines[i], copy)
            erase(*lines[j], copy)
            erase(*lines[k], copy)
            for l in range(MAX_NUM) :
                if copy[l] > 1 :
                    flag = False
                    break
            if flag :
                ans += 1

print(ans)