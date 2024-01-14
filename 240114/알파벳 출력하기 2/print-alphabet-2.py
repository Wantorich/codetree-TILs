# A = 65, Z = 90
# ord, chr

n = int(input())
char = 'A'
for i in range(n) :
    for j in range(n) :
        if i <= j :
            print(char, end=' ')
            next_char = ord(char) + 1
            if next_char > 90 :
                next_char = 'A'
            else :
                next_char = chr(next_char) 
            char = next_char
        else :
            print(' ', end=' ')
    print()