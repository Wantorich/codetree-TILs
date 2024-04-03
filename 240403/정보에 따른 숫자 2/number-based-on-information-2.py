import sys

def find(k) :
    min_s = min_n = sys.maxsize
    for i in range(a, b+1) :
        if places[i] > 0 :
            min_s = min(min_s, abs(i - k))
        elif places[i] < 0 :
            min_n = min(min_n, abs(i - k))
    if min_s <= min_n :
        return True
    else : 
        return False
            

T, a, b = map(int, input().split())
points = [tuple(input().split()) for _ in range(T)]
places = [0] * 1001
cnt = 0

for (c, index) in points :
    index = int(index)
    if c == 'S' :
        places[index] = 1 # S면 1 저장
    else :
        places[index] = -1 # N면 -1 저장

for i in range(a, b+1) :
    if find(i) == True :
        cnt += 1

print(cnt)