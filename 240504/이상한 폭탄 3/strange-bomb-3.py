# 폭탄 정수 배열을 탐색해서 
# 한 숫자가 또 나오는 배열의 인덱스 차이를 계산하고
# 그게 k이하이면 폭탄이 2개 터진거지 
# 폭탄은 처음에만 2개터지고 그 이후에는 1개씩

n, k = map(int,input().split())
bombs = [int(input()) for _ in range(n)]
explode = [False] * n
ans = 0
bomb_num = 0

for i in range(len(bombs)) :
    this_bomb = bombs[i]
    bomb_idx = set()
    temp = i
    for j in range(i+1, len(bombs)) :
        if bombs[j] == this_bomb and j - temp <= k :
            bomb_idx.update([temp, j])
            temp = j
    if bomb_num < len(bomb_idx) :
        bomb_num = len(bomb_idx)
        ans = this_bomb

print(ans)