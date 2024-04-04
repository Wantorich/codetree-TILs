import sys

n = int(input())
arr = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(n):
    arr[i] *= 2

    for j in range(n):
        remaining_arr = [elem for k, elem in enumerate(arr) if k != j]
        # for k in range(n):
        #     if k != j:
        #         remaining_arr.append(arr[k])

        sum_diff = 0
        for k in range(n - 2):
            sum_diff += abs(remaining_arr[k + 1] - remaining_arr[k])

        min_diff = min(min_diff, sum_diff)

    arr[i] //= 2

print(min_diff)