a, b = input().split()
a = int(a)
b = int(b)
bmi = b // ((a/100) ** 2)
print("%d" % bmi)
if bmi > 25:
    print('Obesity')