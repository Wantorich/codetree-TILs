arr_A = [list(map(int, input().split())) for _ in range(3)]
input()
arr_B = [list(map(int, input().split())) for _ in range(3)]

for i in range(3) :
    for j in range(3) :
        print(f'{arr_A[i][j]*arr_B[i][j]}', end=' ')
    print()