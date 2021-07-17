def solution(n):
    a = []
    
    while n >= 3:
        a.append(n%3)
        n = n//3
    a.append(n)
    answer = 0
    a.reverse()
    for i in range(len(a)):
        answer += a[i]*(3**i)
    return answer
