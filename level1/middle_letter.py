def solution(s):

    n = len(s)

    if n%2 == 1:
        answer = s[int(n//2)]
    else:
        answer = s[int(n/2)-1: int(n/2)+1]


    return answer