# N의 자리수만큼 한자리씩 0이면 1으로 넣어봄
# 그렇게 바뀐 배열을 최소거리 구하는 함수에 인자로 넣음
# 함수의 리턴값이 최고인걸로 답으로 설정

def dis(s) :
    dis = 0
    ans = len(s)
    for i in range(len(s)-1) :
        if s[i] == '1' :
            if s[i+1] == '1':
                return 0
            else :
                dis += 1
        else :
            dis += 1
            if s[i+1] == '1' :
                ans = min(ans, dis)   
                dis = 0  
    # print(ans)
    return ans    

N = int(input())
seats = input()
ans = 0

for idx, s in enumerate(seats) :
    if s == '0' :
        temp = seats[:idx] + '1' + seats[idx+1:]
        # print(temp)
        ans = max(ans, dis(temp))

print(ans)