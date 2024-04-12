grid = []
bingo = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
]

def can_win(a, b) :
    exist = [False] * 9
    for i in range(9) :
        if a == temp[i] or b == temp[i] :
            exist[i] = True
    for a, b, c in bingo :
        if exist[a] == True and exist[b] == True and exist[c] == True :
            if temp[a] == temp[b] == temp[c] :
                continue
            return True
    return False

for i in range(3) :
    input_ = list(map(int, input()))
    grid.extend(input_)

nums = list(set(grid))
ans = 0

for i in range(len(nums)) :
    for j in range(i+1, len(nums)) :
        temp = grid
        if can_win(nums[i], nums[j]) :
            ans += 1

print(ans)


# 00 01 02, 10 11 12
# 00 10 20, 01 11 21
# 00 11 22, 02 11 20

# 숫자에서 2개씩 뽑는 경우의 수만큼 빙고 색칠해서 확인하는게 맞는듯