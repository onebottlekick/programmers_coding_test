def solution(d, budget):
    d.sort()
    a = 0
    i = 0
    for val in d:
        if a + val <= budget:
            a += val
            i += 1
        else:
            return i
    return i