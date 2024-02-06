n, k = map(int, input().split())
placed = [0] * 10001
end = 10000

for _ in range(n) :
    index, credit = input().split()
    index = int(index)
    end = max(end, index)
    placed[index] = 1 if credit == 'G' else 2

max_cnt = 0
for i in range(1, end - k + 1) :
    sub_cnt = 0
    for j in range(i, i+k+1) :
        sub_cnt += placed[j]
    max_cnt = max(max_cnt, sub_cnt)

print(max_cnt)