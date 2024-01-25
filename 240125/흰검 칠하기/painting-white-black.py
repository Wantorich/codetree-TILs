MAX_IDX = 1000 * 100
n = int(input())
place = [0] * (2*MAX_IDX+1)
l_cnt = [0] * (2*MAX_IDX+1)
r_cnt = [0] * (2*MAX_IDX+1)
curr = MAX_IDX
for _ in range(n) :
    x, direct = input().split()
    x = int(x)
    if direct == 'R' :
        for i in range(curr, curr+x) :
            if place[i] == 100 :
                continue
            place[i] = 1
            r_cnt[i] += 1 
            if l_cnt[i] >= 2 and r_cnt[i] >= 2 :
                place[i] = 100
        curr += x
    else :
        for i in range(curr-x, curr) :
            if place[i] == 100 :
                continue
            place[i] = -1
            l_cnt[i] += 1
            if l_cnt[i] >= 2 and r_cnt[i] >= 2 :
                place[i] = 100
        curr -= x

f_place = list(filter(lambda x : x != 0, r_cnt))
# print(f_place)
print(place.count(-1), place.count(1), place.count(100))