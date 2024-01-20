def get_n(n) :
    if n <= 2 :
        return n
    
    return get_n(int(n // 3)) + get_n(n-1)

n = int(input())
print(get_n(n))