def solution(nums):
    selection=set(nums)
    if (len(nums)/2)>=len(selection):
        answer=len(selection)
    else:
        answer=len(nums)/2
    
    return answer