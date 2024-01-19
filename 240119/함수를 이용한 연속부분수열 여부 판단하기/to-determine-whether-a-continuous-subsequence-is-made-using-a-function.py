n1, n2 = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

def is_include(arr_A, start_A, arr_B, len_B) :
    j = 0
    for i in range(start_A, start_A+len_B) :
        if arr_A[i] != arr_B[j] :
            return False
        j += 1
    return True

flag = False
for i in range(len(arr_A) - len(arr_B) + 1) :
    if is_include(arr_A, i, arr_B, len(arr_B)) :
        flag = True
        break

print('%s' % 'Yes' if flag else 'No')