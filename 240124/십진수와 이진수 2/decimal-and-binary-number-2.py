binary = [int(num) for num in input()]
dec = 0
for num in binary :
    dec = dec * 2 + num

dec *= 17

new_binary = []
while dec > 0 :
    new_binary.append(dec % 2)
    dec //= 2

for num in new_binary[::-1] :
    print(num, end='')