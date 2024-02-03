binarys = list(input())
idx = -1
is_zero_exist = False
for i in range(len(binarys)) :
    if binarys[i] == '0' : 
        binarys[i] = '1'
        is_zero_exist = True
        break

if not is_zero_exist :
    binarys[-1] = '0'

decimal = int(''.join(binarys), 2)
print(decimal)