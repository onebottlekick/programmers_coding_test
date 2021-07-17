def solution(s):
    n = len(s)
    if n==4 or n==6:
        for i in range(n):
            if s[i].isdigit() is False:
                return False
        return True
    else:
        return False