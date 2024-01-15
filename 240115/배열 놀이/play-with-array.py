n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q) :
    line = list(map(int, input().split()))
    odr, idx = line[0], line[1]
    if odr == 1 :
        print(arr[idx-1])
    elif odr == 2 :
        if idx in arr :
            print(arr.index(idx)+1)
        else :
            print(0)
    elif odr == 3 :
        endex = line[2]
        for i in range(idx-1, endex) :
            print(arr[i], end=' ')