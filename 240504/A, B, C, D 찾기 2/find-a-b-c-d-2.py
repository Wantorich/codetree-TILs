# A, B, C, D, 
# A + B, B + C, C + D, D + A, A + C, B + D, 
# A + B + C, A + B + D, A + C + D, B + C + D, 
# A + B + C + D

nums = list(map(int, input().split()))
nums.sort()

length = len(nums)
# 앞에 4개부터 뽑으면서 가능한 경우의 수를 더해보고
# 배열에 그 더한 값이 존재하는지판단, 존재 안하면 그 숫자는 아닌거임
# 그럼 다음 배열의 경우의 수를 생각해보고

def is_exist(a,b,c,d) :
    arr = [a,b,c,d]
    if sum(arr) not in nums :
        return False
    for n in arr :
        if sum(arr) - n not in nums :
            return False
    for i in range(4) :
        for j in range(i+1, 4) :
            if sum(arr) - (arr[i] + arr[j]) not in nums :
                return False
    return True


for i in range(0, length) :
    for j in range(i+1, length) :
        for k in range(j+1, length) :
            for l in range(k+1, length) :
                    if is_exist(nums[i], nums[j], nums[k], nums[l]) :
                        print(nums[i], nums[j], nums[k], nums[l])
                        break