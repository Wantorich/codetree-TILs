d, h, m = map(int, input().split())
time = m + h * 60 + (d-1) * 24 * 60
target_time = 11 + 11 * 60 + 10 * 24 * 60

if time < target_time :
    print(-1)
else :
    print(time - target_time)