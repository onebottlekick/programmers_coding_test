def solution(s):
    lower_case = [i for i in s if i.islower()]
    upper_case = [j for j in s if j.isupper()]
    return ''.join(sorted(lower_case, reverse=True) + sorted(upper_case, reverse=True))