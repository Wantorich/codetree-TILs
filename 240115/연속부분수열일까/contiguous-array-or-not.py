len_A, len_B = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

# B의 원소들을 각각 A에 있는지 확인하고
# 모두 존재해야하고 인덱스도 연속되야함
temp = -1
flag = True
for num_B in arr_B : 
    if num_B in arr_A :
        idx = arr_A.index(num_B)
        if temp == -1 :
            temp = idx
        else :
            if idx - temp == 1 :
                continue
            else :
                flag = False
                break

print('%s' % 'Yes' if flag else 'No')