def compute(arr) :
    a = arr[0]
    b = arr[1]
    if a < b :
        a += 10
        b *= 2
    else :
        a *= 2 
        b += 10
    arr[0] = a
    arr[1] = b

arr = list(map(int, input().split()))
compute(arr)
print(arr[0], arr[1])