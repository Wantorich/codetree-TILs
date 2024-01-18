word = input()
target = input()

while target in word :
    word_list = list(word)
    for i in range(len(word_list)-len(target)+1) :
        matched = True
        for j in range(len(target)) :
            if word_list[i+j] != target[j] :
                matched = False
                break
        if matched :
            new_word = ''.join(word_list[:i]) + ''.join(word_list[i+len(target):])
            word = new_word
            break
print(word)