word = input()
new_word = ''
for c in word :
    if 'A' <= c <= 'Z' :
        new_word += c.lower()
    else :
        new_word += c.upper()

print(new_word)