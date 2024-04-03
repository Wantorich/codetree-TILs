def palindrom(n) :
    string = list(str(n))
    is_pailndrom = True
    start, end = 0, len(string)-1
    while start < end :
        if string[start] != string[end] :
            is_pailndrom = False
            break
        start += 1
        end -= 1
    return is_pailndrom

x, y = map(int, input().split())
ans = 0
for n in range(x, y+1) :
    if palindrom(n) :
        ans += 1
print(ans)