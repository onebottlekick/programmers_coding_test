def solution(s):
    if len(s)%2 == 1:
        return 0
    a = [s[0]]
    for i in s[1:]:
        if a and (a[-1] == i):
            a.pop()
        else:
            a.append(i)
    return 0 if a else 1