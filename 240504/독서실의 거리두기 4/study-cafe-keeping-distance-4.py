n = int(input())
seats = list(map(int, list(input())))
ans = 0

for i in range(len(seats)) :
    for j in range(i+1, len(seats)) :
        if seats[i] == 1 or seats[j] == 1 :
            continue
        temp = seats[:]
        temp[i] = temp[j] = 1 # 수정된 배열 생성
        init = n
        # print(temp)
        for k in range(len(temp)) :
            if temp[k] == 1 : # start index
                for l in range(k+1, len(temp)) :
                    if temp[l] == 1 :
                        dist = l - k
                        init = min(dist, init)
                        k = l
                break
        # print(init)
        ans = max(ans, init)    

print(ans)