def plus(a,b) :
    return a+b

def minus(a,b) :
    return a-b

def mult(a,b) :
    return a*b

def divide(a,b) :
    if b != 0 :
        return a // b
    else : 
        return False

x, op, y = input().split()
x = int(x)
y = int(y)
if op == '+' :
    res = plus(x,y)
    print(f'{x} {op} {y} = {res}')
elif op == '-' :
    res = minus(x,y)
    print(f'{x} {op} {y} = {res}')
elif op == '*' :
    res = mult(x,y)
    print(f'{x} {op} {y} = {res}')
elif op == '/' :
    res = divide(x,y)
    print(f'{x} {op} {y} = {res}')
else :
    print(False)