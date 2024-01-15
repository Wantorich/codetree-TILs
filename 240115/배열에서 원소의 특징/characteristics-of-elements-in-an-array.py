arr = list(map(int, input().split()))
for i in range(len(arr)) :
    if i > 0 and arr[i] % 3 == 0 :
        print(arr[i-1])
        break