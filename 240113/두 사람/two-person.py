ageA, sexA = input().split()
ageB, sexB = input().split()
if (sexA == 'M' and int(ageA) >= 19) or (sexB == 'M' and int(ageB) >= 19) :
    print(1)
else :
    print(0)