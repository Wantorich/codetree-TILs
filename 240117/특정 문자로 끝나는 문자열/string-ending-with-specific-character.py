words = [
    input()
    for _ in range(10)
]

flag = False
last_char = input()
for word in words :
    if word[-1] == last_char :
        print(word)
        flag = True

if flag == False :
    print('None')