n, k = map(int, input().split())
bomb_set = [int(input()) for _ in range(n)]

max_bomb = -1
for i in range(n) :
    curr_bomb = bomb_set[i]
    for j in range(i+1, min(i+1+k, n)) :
        if curr_bomb == bomb_set[j] :
            max_bomb = max(max_bomb, curr_bomb)

print(max_bomb)