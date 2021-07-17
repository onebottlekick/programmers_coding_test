def solution(s):
    word_2_num_dic = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

    answer = s
    for k in word_2_num_dic.keys():
        if k in answer:
            answer = answer.replace(k, (str(word_2_num_dic[k])))

    return int(answer)

print(solution("2three45sixseven"))