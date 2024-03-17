N, C, G, H = map(int, input().split())
temp = [tuple(map(int, input().split())) for _ in range(N)]

max_output = 0
for t in range(1001) :
    output = 0
    for i in range(N) :
        l, r = temp[i]
        if t < l :
            output += C
        elif t <= r :
            output += G
        else :
            output += H
    max_output = max(max_output, output)

print(max_output)