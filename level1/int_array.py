def solution(n):
    answer = str(n).replace('', '.')[1:-1].split('.')
    answer = list(map(int, answer))
    answer.reverse()
    return answer