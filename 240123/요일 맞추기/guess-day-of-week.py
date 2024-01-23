# 두 날짜의 차이 일수를 구한다
# 만약 15일이다 그럼 현재 요일 + 1일이다

m1, d1, m2, d2 = map(int, input().split())
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

diff_days = sum(num_of_days[:m2]) + d2 - (sum(num_of_days[:m1]) + d1)

if diff_days >= 0 :
    print(days[diff_days % 7])
else :
    print(days[-(abs(diff_days) % 7)])