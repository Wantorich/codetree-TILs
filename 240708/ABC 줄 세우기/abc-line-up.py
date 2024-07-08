N = int(input())
line = input().split()

cnt = 0
alpha = 'A'
while True:
    flag = True
    for i in range(N-1):
        if line[i] != alpha:
            flag = False
            # swap
            line[i], line[i+1] = line[i+1], line[i]
            # print(line)
            cnt += 1
        alpha = chr(ord(alpha)+1) if alpha < 'Z' else 'A'
    alpha = 'A'
    if flag:
        break

print(cnt)