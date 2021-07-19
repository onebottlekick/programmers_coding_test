def solution(s):
    s = s.split(' ')
    answer = []
    for i in s:
        for j in range(len(i)):
            if j%2 == 0:
                i = i[:j] + i[j].upper() + i[j+1:]
            else:
                i = i[:j] + i[j].lower() + i[j+1:]
        answer.append(i)
    answer = ' '.join(answer)
    return answer

print(solution('TRY hello world'))