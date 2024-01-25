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
        curr += x
    else :
        for i in range(curr-x, curr) :
            place[i] = -1
        curr -= x

print(place.count(-1), place.count(1))
# f_place = list(filter(lambda x : x >= 2 ,place))
# print(len(f_place))