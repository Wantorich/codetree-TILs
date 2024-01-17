n = int(input())
total_str = ''
for word in input().split() :
    total_str += word

for i in range(len(total_str)) :
    print(total_str[i], end='')
    if (i+1) % 5 == 0 :
        print()