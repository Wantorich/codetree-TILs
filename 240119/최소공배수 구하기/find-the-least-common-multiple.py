def gcd(a, b) :
  while b != 0 :
    r = a % b
    a = b
    b = r
  return a

def lcm(a,b) :
    return int((a * b) / gcd(a,b))

n, m = map(int, input().split())
print(lcm(n,m))