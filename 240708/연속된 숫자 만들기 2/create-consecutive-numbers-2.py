a, b, c = tuple(map(int, input().split()))

# 1. 이미 정렬되어 있는 경우
# 2. 붙이는 방법 2가지, 왼쪽을 가운데 오른쪽으로 
# 한칸 띄우고 존재하면 다음 순서가 정답임 -> 1 3 19
# 이말은 최대 2번이면 정렬이 가능하단거임
# 그럼 1번 하는 경우의 수는?
# 이미 위 상태에서 시작하는 경우!
# a, a+2, b or a, b-2, b

if a + 1 == b and b + 1 == c:
    print(0)
elif a + 2 == b or b + 2 == c :
    print(1)
else :
    print(2)