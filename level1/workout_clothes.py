n = 5
lost = [4, 2]
reserve = [3, 5]
answer = 5

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    lost = lost
    for j in lost.copy():
        if j-1 in reserve:
            reserve.remove(j-1)
            lost.remove(j)
        elif j+1 in reserve:
            reserve.remove(j+1)
            lost.remove(j)

    return n-len(lost)
print(solution(n, lost, reserve))