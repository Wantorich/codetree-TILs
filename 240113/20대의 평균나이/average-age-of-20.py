s, c = 0, 0
while True :
    age = int(input())
    if age < 20 or age > 29 :
        break
    s += age
    c += 1
print(f'{s/c:.2f}')