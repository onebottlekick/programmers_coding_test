def solution(seoul):
    name_dic = {x:y for x,y in zip(seoul,range(len(seoul)))}
    return f'김서방은 {name_dic["Kim"]}에 있다'