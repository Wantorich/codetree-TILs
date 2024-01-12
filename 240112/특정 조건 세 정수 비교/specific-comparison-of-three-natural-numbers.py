a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
m, e = 0, 0

if a <= b and a <= c :
    m = 1
if a == b == c :
    e = 1
print(m, e)