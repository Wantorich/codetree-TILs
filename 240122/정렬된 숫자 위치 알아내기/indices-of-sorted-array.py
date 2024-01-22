n = int(input())
arr = list(map(int, input().split()))
index_arr = []
for i, num in enumerate(arr) :
    index_arr.append((num, i+1))
# print(index_arr)

index_arr.sort()
# print(index_arr)

rank_arr = [0] * (n+1)
for i, (num, changed) in enumerate(index_arr) :
    rank_arr[changed] = i+1

for rank in rank_arr[1:] :
    print(rank, end=' ')