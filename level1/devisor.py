def check(x):
    a = [i for i in range(1, x+1) if x%i == 0]
    if len(a)%2 == 0:
        print(a)
        return 'even'
    else:
        print(a)
        return 'odd'
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if check(i) == 'even':
            answer += i
        else:
            answer -= i
    return answer
