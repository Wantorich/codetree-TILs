n, k, target = input().split()
words = [
    input()
    for _ in range(int(n))
]
words.sort()
cnt = 0
for word in words :
    if word.startswith(target) :
        cnt += 1
        if cnt == int(k) :
            print(word)
            break