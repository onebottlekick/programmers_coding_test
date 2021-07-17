def check(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def solution(n):
    answer = len([i for i in range(1, n+1) if check(i)])
    return answer-1 # 1 is not prime number

