def lcm(a, b) : 
  return int((a * b) / gcd(a, b))

def gcd(a, b) : 
  while (b != 0) :
    r = a % b
    a = b
    b = r
  return a

# n번째까지의 최소공배수는 n-1번째까지의 최소공배수와의 최소공배수
def get_lcm(n) :
    if n == -1 :
        return 1
    global arr
    return lcm(get_lcm(n-1), arr[n])

n = int(input())
arr = list(map(int, input().split()))
print(get_lcm(n-1))