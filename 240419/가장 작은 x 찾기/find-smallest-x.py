n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

start = ranges[0][0] // 2
end = ranges[0][1] // 2
for x in range(start, end+1) :
    flag = True
    temp = x
    for (s, e) in ranges :
        temp *= 2
        if s > temp or temp > e :
            flag = False
            break
    if flag :
        print(x)
        break