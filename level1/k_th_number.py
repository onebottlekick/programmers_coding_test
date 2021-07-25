def solution(array, commands):
    answer = []
    for i in commands:
        cut_ls = array[i[0]-1 :  i[1]]
        cut_ls.sort()
        answer.append(cut_ls[i[2]-1])
    
    return answer