n, b = map(int, input().split())

digits = []

while n > 0 :
    digits.append(n % b)
    n //= b

for digit in digits[::-1] :
    print(digit, end='')