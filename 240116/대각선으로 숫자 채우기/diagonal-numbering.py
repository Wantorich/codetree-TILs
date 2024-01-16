n, m = map(int, input().split())

# 0,0 / 0,1 1,0 / 0,2 1,1 2,0 / 0,3 1,2 2,1 3,0
# 합이 0, 1, 2

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# cnt = 1
# for j in range(m) :
#     for i in range(j+1) :
#         arr_2d[i][j-i] = cnt
#         cnt += 1

# for i in range(1, n) :
#     k = 0
#     for j in range(m-1, -1, -1) :
#         if i+k >= n :
#             break
#         arr_2d[i+k][j] = cnt
#         k += 1
#         cnt += 1

cnt = 1
x = y = 0
phase_x = 1
phase_y = 0
while x <= n-1 and y <= m-1 :
    arr_2d[x][y] = cnt
    cnt += 1
    x += 1
    y -= 1
    if x >= n or y < 0 :
        phase_y += 1
        if phase_y <= m-1 :
            x = 0
            y = phase_y
        else :
            x = phase_x
            phase_x += 1
            y = m-1        

for row in arr_2d :
    for num in row :
        print(num, end=' ')
    print()