r, c = map(int, input().split())
grid = [list(input().split()) for _ in range(r)]
cnt = 0
start = grid[0][0]
end = grid[r-1][c-1]
for i in range(1, r-2) :
    for j in range(1, c-2) :
        if grid[i][j] != start :
            fst_branch = grid[i][j]
            for k in range(i+1, r-1) :
                for l in range(j+1, c-1) :
                    if grid[k][l] != fst_branch and grid[k][l] != end:
                        cnt += 1

print(cnt)