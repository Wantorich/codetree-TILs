# L에 따라 원소의 개수를 선택해서 1을 더해줌 HOW?
# 즉 경우의 수가 여러개 있을 수있음
# 각 경우의 수에 대해서
# 최대 H가 될수있는 값은 N임
# N개의 원소가 존재하는데 모두 N이상이면 H는  N이기때문

# L로 바꿀수있는 H의 값?
# 최소값을 더해주는게 젤 효율적임

N, L = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0

# H이상인 원소가 H개 이상이라는거는
# [H, ... h개]

for H in range(1, N+1) :
    copy = nums[:]
    for i in range(N) :
        if H - copy[i] == 1 :
            copy[i] += 1
    cnt = 0
    for n in copy :
        if n >= H :
            cnt += 1
        if cnt >= H :
            ans = H
            break
                
print(ans)