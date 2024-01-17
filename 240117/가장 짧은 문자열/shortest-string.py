len_A = len(input())
len_B = len(input())
len_C = len(input())

max_value = max(abs(len_A-len_B), abs(len_A-len_C), abs(len_B-len_C))
print(max_value)