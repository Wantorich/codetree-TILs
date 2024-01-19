m, d = map(int, input().split())
# 4, 6, 9 ,11 -> 30days
# 2 -> 28days

def is_in_2021(m, d) :
    if m == 2 :
        if d > 28 :
            return False
        else :
            return True
    elif m == 4 or m == 6 or m == 9 or m == 11 :
        if d > 30 :
            return False
        else :
            return True
    elif m <= 12 :
        if d > 31 :
            return False
        else :
            return True
    else :
        return False

if is_in_2021(m, d) :
    print('Yes')
else :
    print('No')