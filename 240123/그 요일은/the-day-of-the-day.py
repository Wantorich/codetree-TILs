# m1, d1은 월요일
# 즉 day에 뭐가 주어져도 월요일이 첫 날짜라 생각하면 그 주에 한번은 존재
# 즉 +6일까지 1번, 차이를 7로 나눈 몫
# 몫과 나머지
# 월요일 개수는 몫만큼 있음 
# 타겟이 월요일이면 몫이 답임
# 월요일이 아니라면? 나머지가 타겟의 인덱스보다 크면 +1
# 나머지가 타겟의 인덱스보다 작면 몫이 정답

m1, d1, m2, d2 = map(int, input().split())
day = input()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

diff_days = sum(num_of_days[:m2]) + d2 - (sum(num_of_days[:m1]) + d1)
mon_times = diff_days // 7
remain = diff_days % 7

if day != 'Mon' :
    if days.index(day) <= remain :
        mon_times += 1

print(mon_times+1)