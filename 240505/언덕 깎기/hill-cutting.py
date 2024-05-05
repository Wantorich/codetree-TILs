# 언덕차가 17이어야하니까
# [h, h+17] 사이에 모든 배열이 존재해야함
# 가능한 h를 완전탐색
import sys

n = int(input())
k = 17
heights = [int(input()) for _ in range(n)]
ans = sys.maxsize
MAX_HEIGHT = 100

def get_cost(low, high) :
    cost = 0
    for elem in heights :
        if elem < low :
            cost += (low - elem) ** 2
        elif elem > high :
            cost += (high - elem) ** 2
    return cost 

# 최소 언덕의 최대높이는 83
for height in range(0, MAX_HEIGHT+1-k) :
    ans = min(ans, get_cost(height, height+k))

print(ans)