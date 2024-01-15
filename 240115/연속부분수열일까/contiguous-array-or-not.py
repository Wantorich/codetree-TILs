len_A, len_B = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

# B의 원소들을 각각 A에 있는지 확인하고
# 모두 존재해야하고 인덱스도 연속되야함
# 문제는 2개이상 같은 원소가 존재할수있다는거야
flag = False

len_diff = len_A - len_B
for i in range(len_diff+1) :
    if arr_A[i:i+len_diff] == arr_B :
        flag = True

print('%s' % 'Yes' if flag else 'No')