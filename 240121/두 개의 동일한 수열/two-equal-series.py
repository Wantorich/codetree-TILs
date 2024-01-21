n = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort()
arr_B.sort()
flag = True
for i in range(n) :
    if arr_A[i] != arr_B[i] :
        flag = False
        break

print('%s' % 'Yes' if flag else 'No')