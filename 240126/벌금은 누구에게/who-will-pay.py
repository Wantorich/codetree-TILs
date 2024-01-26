n, m, k = map(int, input().split())
students = [0] * (n+1)
penalty = [int(input()) for _ in range(m)]
res = -1
for index in penalty :
    students[index] += 1
    if students[index] >= k :
        res = index
        break

print(res)