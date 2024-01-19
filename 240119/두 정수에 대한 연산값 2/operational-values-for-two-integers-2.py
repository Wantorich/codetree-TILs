def compute(arr) :
    a = min(arr[0], arr[1])
    b = max(arr[0], arr[1])
    arr[0] = a + 10
    arr[1] = b * 2

arr = list(map(int, input().split()))
compute(arr)
print(arr[0], arr[1])