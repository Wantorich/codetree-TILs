def have_diff_chars(word) :
    # alphabet number is 26
    arr = [0] * 26
    for c in word :
        index = ord(c) - ord('a')
        if arr[index] > 0 :
            return True
        else :
            arr[index] += 1

word = input()
if have_diff_chars(word) :
    print('Yes')
else :
    print('No')