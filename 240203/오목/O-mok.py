size = 19
grid = [list(map(int, input().split())) for _ in range(size)]

winner = 0
x, y = -1, -1

def in_range(i, j) :
    global size
    return 0 <= i < size and 0 <= j < size

def is_win_horizon(i, j) :
    curr = grid[i][j]
    for k in range(4) :
        j += 1
        if in_range(i,j) and grid[i][j] != curr :
            return False
    return True

def is_win_vertical(i, j) :
    curr = grid[i][j]
    for k in range(4) :
        i += 1
        if in_range(i,j) and grid[i][j] != curr :
            return False
    return True

def is_win_cross(i, j) :
    curr = grid[i][j]
    for k in range(1, 5) :
        x, y = i+k, j+k
        if in_range(x,y) and grid[x][y] != curr :
            return False

    for k in range(1, 5) :
        x, y = i-k, j-k
        if in_range(x,y) and grid[x][y] != curr :
            return False

    return True



for i in range(size) :
    for j in range(size) :
        if grid[i][j] != 0 :
            if is_win_horizon(i, j) :
                winner = grid[i][j]
                x, y = i, j+2
            if is_win_vertical(i, j) :
                winner = grid[i][j]
                x, y = i+2, j
            if is_win_cross(i,j) :
                winner = grid[i][j]
                x, y = i+2, j+2

print(winner)
print(x+1, y+1)