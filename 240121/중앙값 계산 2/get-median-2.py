# 1, 3, 5, 7 번째에 읽음
n = int(input())
arr = list(map(int, input().split()))

center = []
for i, v in enumerate(arr) :
    center.append(v)
    center.sort()
    if i % 2 == 0 :
        medien = center[(len(center)-1) // 2]
        print(medien, end=' ')