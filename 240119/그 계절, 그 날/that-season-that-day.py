y, m, d = map(int, input().split())

def is_exist_month_day(is_Yoon, m, d) :
    if m == 2 :
        last_day = 29 if is_Yoon else 28
        if d > last_day :
            return False
    elif m == 4 or m == 6 or m == 9 or m == 11 :
        if d > 30 :
            return False
    elif m <= 12 :
        if d > 31 :
            return False
    else :
        return False
    return True

def is_yoon_year(y) :
    if y % 4 == 0 :
        if y % 100 == 0 :
            if y % 400 == 0 :
                return True
            return False
        return True
    else :
        return False        

def is_exist(y,m,d) :
    if is_yoon_year(y) :
        # 2 -> 29
        if is_exist_month_day(True, m, d) :
            return True
    else :
        if is_exist_month_day(False, m, d) :
            return True
    return False

if is_exist(y, m, d) :
    if m <= 2 :
        print('Winter')
    elif m <= 5 :
        print('Spring')
    elif m <= 8 :
        print('Summer')
    elif m <= 11 :
        print('Fall')
    else :
        print('Winter')


    # if 3 <= m <= 5 :
    # elif 6 <= m <= 8 :
    # elif 9 <= m <= 11 :
    # elif 12 <= m or m >= 1 :
else :
    print(-1)