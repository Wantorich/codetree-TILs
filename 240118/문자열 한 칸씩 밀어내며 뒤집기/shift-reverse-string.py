word, n = input().split()

for _ in range(int(n)) :
    c = input()
    if c == '1' :
        word = word[1:] + word[0] 
        print(word)
    elif c == '2' :
        word = word[-1] + word[:-1]
        print(word)
    elif c == '3' :
        new_word = ''
        for j in range(1, len(word)+1) :
            new_word += word[-1*j]
        word = new_word
        print(word)