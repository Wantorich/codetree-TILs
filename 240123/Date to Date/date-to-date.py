m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date_1 = sum(num_of_days[:m1+1]) + d1
date_2 = sum(num_of_days[:m2+1]) + d2
if date_2 - date_1 <= 0 :
    print(1)
else :
    print(date_2 - date_1)