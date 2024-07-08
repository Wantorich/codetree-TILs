# 1, 2, 3을 배치할수있는 경우의수가 6개
# 이기는 횟수가 최대값이니, 다른 경우의 수만 따지면 됌
# 1로 3을 이기면, 자연스레 3이 2를 이김
# (1,3) (3,2) / 
l = [1, 2, 3]

N = int(input())
matches = [tuple(map(int, input().split())) for _ in range(N)]

# 숫자가 다르면 1번 개발자가 이기는 경우와 지는 경우가 있음
setted = False
win_cnt = [0] * 2
for a, b in matches:
    if a == b:
        continue

    # a가 b를 이긴다고 가정
    # a는 c한테 지고, b는 c한테 이기게됌
    if not setted:
        x = a
        y = b
        l.remove(a)
        l.remove(b)
        z = l[0]
        setted = True

    if (a == x and b == y) or (a == y and b == z) or (a == z and b == x):
        win_cnt[0] += 1    

l = [1, 2, 3]
setted = False
for a, b in matches:
    if a == b:
        continue

    # b가 a를 이긴다고 가정
    # c는 a한테 지고, c는 b한테 이기게됌
    if not setted:
        x = b
        y = a
        l.remove(a)
        l.remove(b)
        z = l[0]
        setted = True

    if (a == x and b == y) or (a == z and b == x) or (a == y and b == z):
        win_cnt[1] += 1    

print(max(win_cnt))