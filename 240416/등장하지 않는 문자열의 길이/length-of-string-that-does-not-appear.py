n = int(input())
sentence = input()

ans = 1
while True :
    temp = {}
    for i in range(n-ans+1) :
        word = sentence[i:i+ans]
        temp[word] = temp[word]+1 if word in temp else 1
    # print(temp)
    flag = False
    for _, v in temp.items() :
        if v == 2 :
            ans += 1 
            flag = True
            break
    if flag :
        continue
    break

print(ans)

# 배열로 만들어서
# ans를 1씩 증가시키며 for문으로 탐
# slice로 j : j+i