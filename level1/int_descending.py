def solution(n):
    n =  str(n).replace('', ',')[1:-1].split(',')
    n.sort()
    n.reverse()
    answer = int(''.join(n))
    return answer