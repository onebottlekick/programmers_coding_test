def solution(numbers, hand):
    l_list = [1, 4, 7]
    r_list = [3, 6, 9]
    btn_dic = {1:(0,0), 2:(0,1), 3:(0,2),
              4:(1,0), 5:(1,1), 6:(1,2),
               7:(2,0), 8:(2,1), 9:(2,2),
               '*':(3,0), 0:(3,1), '#':(3,2)
              }
    l_current = (3,0)
    r_current = (3,2)
    result_list = []
    for i in numbers:
        if i in l_list:
            result_list.append('L')
            l_current = btn_dic[i]
        elif i in r_list:
            result_list.append('R')
            r_current = btn_dic[i]
        else:
            l_dis = abs(l_current[0]-btn_dic[i][0]) + abs(l_current[1]-btn_dic[i][1])
            r_dis = abs(r_current[0]-btn_dic[i][0]) + abs(r_current[1]-btn_dic[i][1])
            if l_dis > r_dis:
                result_list.append('R')
                r_current = btn_dic[i]
            elif l_dis < r_dis:
                result_list.append('L')
                l_current = btn_dic[i]
            else: 
                if hand == 'right':
                    result_list.append('R')
                    r_current = btn_dic[i]
                else:
                    result_list.append('L')
                    l_current = btn_dic[i]
                    
    answer = ''.join(result_list)
    return answer