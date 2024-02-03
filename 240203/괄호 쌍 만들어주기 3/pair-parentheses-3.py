brackets = list(input())
cnt = 0
for i in range(len(brackets)) :
    if brackets[i] == '(' :
        for close in brackets[i+1:] :
            if close == ')' :
                cnt += 1

print(cnt)