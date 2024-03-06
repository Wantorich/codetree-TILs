# 직사각형의 넓이를 최소로하려면
# 점들 중에서 y값의 최소, 최대 구하고
# x값의 최소 최대 구해서 넓이구하면됨
import sys

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize
for i in range(n):
    # count = [0] * 11 # initialize
    left, right = 40000, 1
    top, bottom = 1, 40000
    for j in range(n):
        if j == i:
            continue
        x, y = segments[j]
        left = min(left, x)
        right = max(right, x)
        top = max(top, y)
        bottom = min(bottom, y)
        # print(left, right, top, bottom)
        # x1, x2 = segments[j]
        # for k in range(x1, x2 + 1):
        #     count[k] += 1

    area = (right - left) * (top - bottom)
    ans = min(ans, area)
    # max_cnt = max(count)
    # ans = min(ans, max_cnt)

print(ans)