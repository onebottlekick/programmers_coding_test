def solution(absolutes, signs):
    answer_ls = []
    
    for ind, num in enumerate(absolutes):
        if signs[ind] == True:
            answer_ls.append(num)
        else:
            answer_ls.append(-num)
    answer = sum(answer_ls)
    return answer