n = int(input())
words = list(input())
cnt = 0
for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            if words[i] == 'C' and words[j] == 'O' and words[k] == 'W' :
                cnt += 1

print(cnt)