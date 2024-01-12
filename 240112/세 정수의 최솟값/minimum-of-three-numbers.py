a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a <= b :
    if a <= c :
        print(a)
    else :
        print(c)
else :
    print(b)