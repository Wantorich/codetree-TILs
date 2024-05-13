# 몇번의 비둘기가 2번이상 정보가 나오고
# 위치가 바뀌어야 최소 옮긴 카운트 수가 올라감
# N만큼 배열을 잡고 배열의 값을 바꿔주는걸로 판단

n = int(input())
arr = [-1] * (11)
ans = 0

for i in range(n) :
    bird, place = map(int,input().split())
    if arr[bird] == -1 : # 첫 정보
        arr[bird] = place
    else : # 이미 정보가 앞에서 주어진 경우
        if arr[bird] != place :
            ans += 1
            arr[bird] = place

print(ans)