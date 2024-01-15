n = int(input())
cnt = 0
for _ in range(n) :
    grade_arr = list(map(int, input().split()))
    sub_sum = 0
    for grade in grade_arr :
        sub_sum += grade
    if sub_sum // len(grade_arr) >= 60 :
        print('pass')
        cnt += 1
    else :
        print('fail')
print(cnt)