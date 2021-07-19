def solution(num):
    iter = 0
    while iter < 500:
        if num%2 == 0:
            num /= 2
            iter += 1
        else:
            if num == 1:
                return iter
            else:
                num = num*3 + 1
                iter += 1
    return -1