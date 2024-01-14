a, b = map(int, input().split())
suf = ''
for _ in range(14) :
    suf += '0'
print(f'{a/b:f}{suf}')