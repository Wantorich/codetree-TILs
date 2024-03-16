n, m, d, s = map(int, input().split())
notes = [list(map(int, input().split())) for _ in range(d)]
pains = [tuple(map(int, input().split())) for _ in range(s)]
ans = 0
corrupt = []
suspect = [[] for _ in range(s)]
for i in range(s) :
    # 아픈 기록을 보고 탐색
    who, when = pains[i]
    notes.sort() #사람 기준으로 정렬
    # print(notes)
    for j in range(d) :
        if who == notes[j][0] and when >= notes[j][2] + 1 :
            suspect[i].append(notes[j][1])
            # if not notes[j][1] in corrupt :
            #     corrupt.append(notes[j][1])

# print(suspect)
for cheese in suspect[0] :
    flag = True
    for j in range(s) :
        if not cheese in suspect[j] :
            flag = False 
    if flag :
        corrupt.append(cheese)


# 아픈사람은 의심되는 치즈를 무조건 먹었어야해
# print(corrupt)
for cheese in corrupt :
    num = 0
    for j in range(d) :
        if notes[j][1] == cheese :
            num += 1
    ans = max(ans, num)

print(ans)