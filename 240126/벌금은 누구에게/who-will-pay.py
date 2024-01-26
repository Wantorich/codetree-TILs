n, m, k = map(int, input().split())
students = [0] * n
penalty = [int(input())-1 for _ in range(m)]
res = -1
for index in penalty :
    students[index] += 1
    if students[index] >= k :
        res = index + 1

print(res)