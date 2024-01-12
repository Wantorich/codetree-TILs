statusA, degA = input().split()
statusB, degB = input().split()
statusC, degC = input().split()

count = 0
if statusA == 'Y' and int(degA) >= 37 :
    count += 1
if statusB == 'Y' and int(degB) >= 37 :
    count += 1
if statusC == 'Y' and int(degC) >= 37 :
    count += 1

if count >= 2 :
    print('E')
else :
    print('N')