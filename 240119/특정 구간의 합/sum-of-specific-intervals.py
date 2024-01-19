n, m = map(int, input().split())
list_ = list(map(int, input().split()))
for _ in range(m) :
    s, e = map(int, input().split())
    print(sum(list_[s-1:e]))