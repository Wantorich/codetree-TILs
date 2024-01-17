n = int(input())
lines = [
    input()
    for _ in range(n)
]
last_char = input()

total = cnt = 0
for line in lines :
    if line[0] == last_char :
        total += len(line)
        cnt += 1

print(f'{cnt} {total / cnt:.2f}')