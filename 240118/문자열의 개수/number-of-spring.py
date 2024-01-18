idx = 0
array = []
line = input()
while line != '0' :
    array.append(line)
    line = input()

print(len(array))
for i in range(0, len(array), 2) :
    print(array[i])