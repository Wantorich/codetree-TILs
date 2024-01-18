array = input().split()
total = 0
for word in array :
    num = ''
    for c in word :
        if c.isdigit() :
            num += c
        else :
            break
    if num != '' :
        total += int(num)
print(total)