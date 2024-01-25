MAX_IDX = 1000 * 100
n = int(input())
place = [0] * (2*MAX_IDX+1)
curr = MAX_IDX
for _ in range(n) :
    x, direct = input().split()
    x = int(x)
    if direct == 'R' :
        for i in range(curr, curr+x) :
            place[i] = 1
        curr += x - 1
    else :
        for i in range(curr, curr-x, -1) :
            place[i] = -1
        curr -= x - 1

print(place.count(-1), place.count(1))