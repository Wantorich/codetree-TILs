n = int(input())
nums = [int(input()) for _ in range(n)]

def is_carry(x,y,z) :
    while x != 0 or y != 0 or z != 0:
        remain_add = (x % 10) + (y % 10) + (z % 10)
        if remain_add >= 10 :
            return True
        x, y, z = x // 10, y // 10, z // 10
    return False

max_val = -1
for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            if not is_carry(nums[i], nums[j], nums[k]) :
                max_val = max(max_val, nums[i] + nums[j] + nums[k])

print(max_val)