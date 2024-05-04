# 배열을 정렬해서 최대값에서 최소값 뺀게 17이하여야함
# 17 초과이면 최대값을 두번째 최대값까지 깎던가

n = int(input())
heights = [int(input()) for _ in range(n)]
cost = 0
heights.sort()

def minmax() :
    return max(heights) - min(heights)

diff = heights[-1] - heights[0]
if diff > 17 :
    cutting = diff - 17
    for i in range(1, cutting) :
        max_val = heights[-1]
        min_val = heights[0]
        heights[0] += i
        heights[-1] -= cutting - i
        # print(heights)
        if minmax() <= 17 :
            cost = i**2 + (cutting-i)**2
            break
        heights[0] = min_val
        heights[-1] = max_val

print(cost)