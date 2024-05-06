squares = [list(map(int, input().split())) for _ in range(2)]

if squares[0][2] < squares[1][0] or squares[1][2] < squares[0][0] or squares[0][3] < squares[1][1] or squares[1][3] < squares[0][1] :
    print('nonoverlapping')
else :
    print('overlapping')