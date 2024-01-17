lines = [
    input()
    for _ in range(2)
]

for line in lines :
    for char in line :
        if char != ' ' :
            print(char, end='')