def have_diff_chars(word) :
    # alphabet number is 26
    arr = [0] * 26
    cnt = 0
    for c in word :
        if cnt >= 2 :
            return True
        index = ord(c) - ord('a')
        if arr[index] == 0 :
            cnt += 1
        arr[index] += 1
    return False

word = input()
if have_diff_chars(word) :
    print('Yes')
else :
    print('No')