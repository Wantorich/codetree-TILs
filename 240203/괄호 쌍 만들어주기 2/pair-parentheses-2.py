brackets = list(input())
length = len(brackets)
cnt = 0
for i in range(length) :
    for j in range(i+2, length-1) :
        if brackets[i] == '(' and brackets[i+1] == '(' and brackets[j] == ')' and brackets[j+1] == ')' :
            cnt += 1             
print(cnt)