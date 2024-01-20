# n 개중에서 최댓값 구하기
# n-1 까지의 최댓값과 n번째를 비교한다
# length를 최대값으로 잡고 인덱스를 증가시키면서 비교?
def is_max(n) :
    global arr
    if n == 0 :
        return -1
    return max(arr[n], is_max(n-1))

n = int(input())
arr = list(map(int, input().split()))
print(is_max(n-1))