array = [
    input()
    for _ in range(2)
]
total = 0
for line in array :
    num = ''
    for c in line :
        if c.isdigit() :
            num += c
    total += int(num)
print(total)