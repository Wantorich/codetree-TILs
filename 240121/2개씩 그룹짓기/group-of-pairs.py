# 정렬하고 처음이랑 끝이랑 그룹하면 최소
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
i = 0
max_ = 0
while i <= len(arr)-i-1 :
    add_ = arr[i] + arr[len(arr)-1-i]
    if add_ >= max_ :
        max_ = add_
    i += 1

print(max_)