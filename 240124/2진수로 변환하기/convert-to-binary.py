n = int(input())
digits = []

if n == 0 :
    digits.append(0)

while n > 0:
    digits.append(n % 2)
    n //= 2

for digit in digits[::-1] :
    print(digit, end='')