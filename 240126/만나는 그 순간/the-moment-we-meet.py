n, m = map(int, input().split())
move_a = []
move_b = []
sum_ = 0
for _ in range(n) :
    direct, distance = input().split()
    distance = int(distance)
    sum_ += distance
    if direct == 'L' :
        distance = -distance
    move_a.append(distance)

for _ in range(m) :
    direct, distance = input().split()
    distance = int(distance)
    if direct == 'L' :
        distance = -distance
    move_b.append(distance)


heatmap_a = [0] * sum_
heatmap_b = [0] * sum_

i = 0
for mov in move_a :
    if mov > 0 :
        while mov > 0 :
            if i == 0 :
                heatmap_a[i] = 1
            else :
                heatmap_a[i] = heatmap_a[i-1] + 1
            i += 1
            mov -= 1
    else :
        while mov < 0 :
            if i == 0 :
                heatmap_a[i] = -1
            else :
                heatmap_a[i] = heatmap_a[i-1] - 1
            i += 1
            mov += 1

j = 0
for mov in move_b :
    if mov > 0 :
        while mov > 0 :
            if j == 0 :
                heatmap_b[j] = 1
            else :
                heatmap_b[j] = heatmap_b[j-1] + 1
            j += 1
            mov -= 1
    else :
        while mov < 0 :
            if j == 0 :
                heatmap_b[j] = -1
            else :
                heatmap_b[j] = heatmap_b[j-1] - 1
            j += 1
            mov += 1

# print(heatmap_a)
# print(heatmap_b)

result = -1
for i in range(sum_) :
    if heatmap_a[i] == heatmap_b[i] :
        result = i+1
        break
    
print(result)