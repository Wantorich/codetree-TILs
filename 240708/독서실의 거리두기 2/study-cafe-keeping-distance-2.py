N = int(input())
seats = list(input())

# 양 끝이 1인지 0인지
# 1이 처음 발생한 곳부터 마지막에 나타난곳까지 탐색해서
# 가장 넓은 공백을 지닌 곳을 탐색하고
# 양끝이랑 비교 
# 가장 넓은 공간에 넣음
# 양끝이 0인경우 무조건 끝에 넣는게 이득임

l_space = seats.index('1')
# 0 0 0 1
for i in range(N):
    if seats[i] == '1':
        last_idx = i
r_space = N-1 - last_idx
# 1 0 0 0 0
# 0 1 1 1 0 0 -> 3
# 0 0 1 1 1 0 -> 2

l = seats.index('1')
max_space = 0
for i in range(seats.index('1')+1, N):
    # 1 0 0 0 1, 1 0 0 0 0 1
    if seats[i] == '1':
        r = i
        space = r-1 - l
        if space > max_space:
            max_space = space
            max_l = l
            max_r = r
        l = r

insert_idx = (max_l+max_r)//2
seats[insert_idx] = '1'
# print(''.join(seats))

# print((max_l+max_r)//2 - max_l, l_space-1, r_space-1)
result = max(insert_idx - max_l, l_space-1, r_space-1)
print(result)


# 한쪽만 1이있는경우와 양쪽에 1이 있는경우를 나누는경우
# 전자는 무조건 끝에 배치하는게 이득