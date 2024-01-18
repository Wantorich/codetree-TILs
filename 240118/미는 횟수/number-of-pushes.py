word = input()
target = input()

idx = -1
for i in range(len(word)) :
    shift_word = word[-1] + word[:-1]
    if shift_word == target :
        idx = i+1
        break
    word = shift_word
print(idx)