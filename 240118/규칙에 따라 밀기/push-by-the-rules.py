word = input()
command = input()

for c in command :
    if c == 'L' :
        word = word[1:] + word[0] 
    elif c == 'R' :
        word = word[-1] + word[:-1]
print(word)