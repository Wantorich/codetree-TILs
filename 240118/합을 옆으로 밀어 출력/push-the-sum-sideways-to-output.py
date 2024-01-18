n = int(input())
total = 0
for _ in range(n) :
    total += int(input())
shift_num = str(total)
print(shift_num[1:] + shift_num[0])