line = input()
binary = [int(num) for num in line]
# binary = list(map(int, input().split('')))
num = 0

for i in range(len(binary)):
    num = num * 2 + binary[i]

print(num)