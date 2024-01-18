word = list(input())
target = word[1]
for i in range(len(word)) :
    if word[i] == target :
        word[i] = word[0]
print(''.join(word))