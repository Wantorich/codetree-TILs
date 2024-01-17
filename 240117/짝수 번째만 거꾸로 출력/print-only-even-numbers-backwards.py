line = input()
even_line = [v for i, v in enumerate(line) if i % 2 == 1]
for i in range(1, len(even_line)+1) :
    print(even_line[i*-1], end='')