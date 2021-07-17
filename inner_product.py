def solution(a, b):
    answer_list = []
    for i in  range(len(a)):
            answer_list.append(a[i]*b[i])
            
    answer = sum(answer_list)
    return answer