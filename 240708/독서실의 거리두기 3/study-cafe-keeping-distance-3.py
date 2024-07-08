N = int(input())
seats = list(input())

# 가장 가까운 두사람의 거리를 최대로 하려면 두 자리의 가운데에 놔야겠지
# 그럴려면 제일 빈자리가 넓은곳에 놓으면 좋을테고
# 그럼 일단 간격이 제일 넓은 곳을 찾고, 거기의 가운데에 넣는다

l = 0
max_dis = 0
min_dis = N
for i in range(1, N-1):
    if seats[i] == '1':
        r = i
        dis = r - l
        min_dis = min(min_dis, dis)
        if dis > max_dis:
            max_dis = dis
            max_l = l
            max_r = r
        l = r

insert = (max_r - max_l) // 2 + max_l
seats[insert] = '1'
# print(''.join(seats))
print(min(min(max_r - insert, insert - max_l), min_dis))

# 1 0 0 0 1
# 1 0 0 0 0 1