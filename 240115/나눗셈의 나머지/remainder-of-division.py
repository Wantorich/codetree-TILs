dividend, divisor = map(int, input().split())

remains = [0] * (divisor + 1)
while dividend > 1 :
    remain = dividend % divisor
    dividend //= divisor
    remains[remain] += 1

total = 0
for cnt in remains :
    if cnt > 0 :
        total += cnt**2

print(total)