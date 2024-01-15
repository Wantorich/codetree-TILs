n = int(input())
arr = list(map(int, input().split()))

# sorting이 이미 돼있음
# 차가 최소려면 바로 옆에있는거랑 뺴야함, 2칸 떨어져있는거는 필연적으로 최소일수가 없음

min_sub = arr[-1]
for i in range(1, n) :
    sub = arr[i] - arr[i-1]
    if sub <= min_sub :
        min_sub = sub

print(min_sub)