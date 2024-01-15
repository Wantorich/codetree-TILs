n = int(input())
arr = list(map(int, input().split()))

for i in range(2) :
    for j in range(len(arr)-i-1) :
        if arr[j] > arr[j+1] :
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr[-1], arr[-2])