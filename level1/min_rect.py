def solution(sizes):
    sizes = sorted(sizes, key=lambda x: max(x))
    maxv = max(sizes[-1])
    minv = 0
    for i in sizes:
        if minv < min(i):
            minv = min(i)
    return maxv*minv