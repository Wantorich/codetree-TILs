word = list(input())
for i in range(len(word)) :
    if word[i] == 'e' :
        new_word = ''.join(word[:i]) + ''.join(word[i+1:])
        print(new_word)
        break