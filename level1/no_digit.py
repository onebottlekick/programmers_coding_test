def solution(numbers):
    answer = sum(set([i for i in range(10)]) - set(numbers))
    return answer