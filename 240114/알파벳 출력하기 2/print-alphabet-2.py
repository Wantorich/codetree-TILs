# A = 65, Z = 90
# ord, chr

n = int(input())
char = 'A'
for i in range(n) :
    for j in range(n) :
        if i <= j :
            print(char, end=' ')
            char = chr(ord(char) + 1)
        else :
            print(' ', end=' ')
    print()