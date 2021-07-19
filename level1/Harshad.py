def solution(x):
    sum_x = sum(map(int, [i for i in str(x)]))
    if x % sum_x == 0:
        return True
    else:
        return False