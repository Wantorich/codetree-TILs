# 직각 삼각형을 구하는 문제
# 직각 삼각형 특징, 2개는 y가 같고, 2개는 x가 같음
# 피타고라스를 이용하자
import math

def dist(i, j) :
    x1, y1 = points[i]
    x2, y2 = points[j]
    return ((x2-x1) ** 2) + ((y2-y1) ** 2)

def get_area(i, j, k) :
    lens = [dist(i,j), dist(i,k), dist(j,k)]
    lens.sort()
    if lens[0] + lens[1] != lens[2] :
        return 0
    return int(math.sqrt(lens[0]*lens[1]))

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            ans = max(ans, get_area(i,j,k))

print(ans)