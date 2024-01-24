a, b = map(int, input().split())
n = input()

reverse_a = 0
for num in n :
    reverse_a = reverse_a * a + int(num)

num_by_b = []
while reverse_a > 0 :
    num_by_b.append(reverse_a % b)
    reverse_a //= b

for num in num_by_b[::-1] :
    print(num, end='')