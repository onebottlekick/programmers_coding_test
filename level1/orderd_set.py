def solution(arr):
    # a = ''.join(map(str, arr))
    # for i in a:
    #     while 2*i in a:
    #         a = a.replace(2*i, i)
    # answer = [int(i) for i in a]
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer