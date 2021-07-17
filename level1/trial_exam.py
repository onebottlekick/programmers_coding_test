def solution(answers):
    n = len(answers)
    pattern_1 = ([1,2,3,4,5]*2000)[:n]
    pattern_2 = ([2,1,2,3,2,4,2,5]*1250)[:n]
    pattern_3 = ([3,3,1,1,2,2,4,4,5,5]*1000)[:n]

    result_dict = {}

    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(n):
        if answers[i] == pattern_1[i]:
            count1 += 1
        if answers[i] == pattern_2[i]:
            count2 += 1
        if answers[i] == pattern_3[i]:
            count3 += 1
    
    answer = []
    result = max(count1, count2, count3)
    if(result == count1):
        answer.append(1)
    if(result == count2):
        answer.append(2)
    if(result == count3):
        answer.append(3)
    answer.sort()
    return answer