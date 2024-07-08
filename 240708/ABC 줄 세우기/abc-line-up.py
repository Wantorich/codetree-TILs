N = int(input())
line = input().split()

# cnt = 0
# alpha = 'A'
# while True:
#     flag = True
#     for i in range(N-1):
#         if line[i] != alpha:
#             flag = False
#             # swap
#             line[i], line[i+1] = line[i+1], line[i]
#             # print(line)
#             cnt += 1
#         alpha = chr(ord(alpha)+1)
#     alpha = 'A'
#     if flag:
#         break

# print(cnt)

cnt = 0
alpha = 'A'
# 끝부터 채운다
for i in range(N):
    alpha = chr(ord('A')+i)
    target_idx = line.index(alpha)
    line.insert(i, line[target_idx])
    line.pop(target_idx+1)
    cnt += target_idx - i
    # print(''.join(line))

print(cnt)