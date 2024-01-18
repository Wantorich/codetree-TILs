word, q = input().split()
word = list(word)
for _ in range(int(q)) :
    command = input().split()
    if command[0] == '1' :
        _, l, r = map(int, command)
        temp = word[l-1]
        word[l-1] = word[r-1]
        word[r-1] = temp
        print(''.join(word))
    elif command[0] == '2' :
        _, t, c = command
        for i in range(len(word)) :
            if word[i] == t :
                word[i] = c
        print(''.join(word))