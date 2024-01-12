a, b, c = map(int, input().split())

if a > b :
    if b > c :
        print(b)
    else :
        print('%d' % a if a < c else c)
else :
    if a > c :
        print(a)
    else :
        print('%d' % b if b < c else c)