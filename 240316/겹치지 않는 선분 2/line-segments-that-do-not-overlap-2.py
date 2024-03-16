# 선분이 겹치려면 한 범위 안에 (x1, x2) 
# 다른 선분이 이 안에 완전히 포함되어야함
def in_range(i, j) :
    # i가 j에 포함되는지
    x1, x2 = lines[i]
    x3, x4 = lines[j]
    return x3 < x1 and x2 < x4

# MAX_INT = 1000000
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
ans = n
# grid = [0] * 2 * MAX_INT
for i in range(1, n-1) :
    prev_, curr_, next_ = lines[i-1][1], lines[i][1], lines[i+1][1]
    # 원래는 curr < next 여야함
    if curr_ > next_ or prev_ > curr_ :
        ans -= 1

print(ans)

# for i in range(n) :
    
#     for j, (x1, x2) in enumerate(lines) :
#         include = True
#         x1 += MAX_INT
#         x2 += MAX_INT
#         for k in range(x1, x2) :
#             if grid[k] == 0