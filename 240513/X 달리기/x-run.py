# 결국 꺾이는곳을 찾는것이 관건
# 숫자가 1, 2, 3, ... n, n-1, n-2 ... 1
# 합은 (1+2+3+...+n-1) * 2 + n + 1(마지막 속도 유지)*x= dis
# 근데 이거의 맹점은 마지막 1ms 유지구간이 1초가 아닐수도있다는거임
# n^2 + x = dis
# 이거로 n의 최대값을 찾고 거리를 따로 구한다


dis = int(input())
speed = 1
ans = 0

while dis > 0 :
    if speed**2 <= dis <= (speed+1)**2 :
        dis -= speed**2
        ans += speed*2 - 1
        speed = 1
    else :
        speed += 1
    
print(ans)