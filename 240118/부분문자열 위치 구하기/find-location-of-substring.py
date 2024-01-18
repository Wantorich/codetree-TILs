target_line = input()
word = input()
idx = -1
for i in range(len(target_line) - len(word) + 1) :
    all_match = True
    for j in range(len(word)) :
        if target_line[i+j] != word[j] :
            all_match = False
    if all_match :
        idx = i
        break 

print(idx)