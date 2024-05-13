# 그냥 오른쪽부터 부족한만큼 왼쪽의 남는집에서 옮겨주면 되는거아닌가?

n = int(input())
prev_ = list(map(int, input().split()))
next_ = list(map(int, input().split()))
remain = [prev_[i] - next_[i] for i in range(n)]
ans = 0

for i in range(n-1, -1, -1) :
    if remain[i] < 0 :
        for j in range(0, i) :
            if remain[j] > 0 :
                diff = min(abs(remain[j]), abs(remain[i]))
                remain[j] -= diff
                remain[i] += diff
                ans += (i-j) * diff
            if remain[i] == 0 :
                break

print(ans)