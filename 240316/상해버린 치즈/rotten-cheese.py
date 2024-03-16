n, m, d, s = map(int, input().split())
notes = [list(map(int, input().split())) for _ in range(d)]
pains = [tuple(map(int, input().split())) for _ in range(s)]
ans = 0
corrupt = []
for i in range(s) :
    # 아픈 기록을 보고 탐색
    who, when = pains[i]
    notes.sort() #사람 기준으로 정렬
    for j in range(d) :
        if who == notes[j][0] and when >= notes[j][2] + 1 :
            if not notes[j][1] in corrupt :
                corrupt.append(notes[j][1])

for cheese in corrupt :
    num = 0
    for j in range(d) :
        if notes[j][1] == cheese :
            num += 1
    ans = max(ans, num)

print(ans)