def solution(n):
    answer = ['수' if i%2==0 else '박' for i in range(0, n)]
    answer = ''.join(answer)
    return answer