def solution(N, stages):
    
    cur_pass_dic = {}
    for i in range(max(stages)):
        cur_pass_dic[i+1] = stages.count(i+1)
    fail_rate = {}
    for i in range(N):
        if sum(list(cur_pass_dic.values())[i:]) == 0:
            fail_rate[i+1] = 0
        else:
            fail_rate[i+1] = cur_pass_dic[list(cur_pass_dic.keys())[i]] / sum(list(cur_pass_dic.values())[i:])
    answer_list = sorted(fail_rate.items(), key=lambda x:x[1], reverse=True)
    answer = [i for i,j in answer_list]
    return answer