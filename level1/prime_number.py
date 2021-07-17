def check(x, y, z):
    sum = x + y + z
    for i in range(2, sum):
        if sum%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    n = len(nums)
    # itertools.combination
    for i in range(0, n-2):  
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if check(nums[i], nums[j], nums[k]):
                    answer += 1
    return answer
