n = int(input())
students = []
for i in range(1, n+1) :
    h, w = map(int, input().split())
    students.append((h, w, i))

students.sort(key=lambda x : (x[0], -x[1]))

for h, w, i in students :
    print(h, w, i)