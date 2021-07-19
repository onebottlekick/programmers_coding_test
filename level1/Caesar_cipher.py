# def solution(s, n):
#     answer = []
#     for i in s:
#         if i == ' ':
#             answer.append(i)
#         else:    
#             if ord(i)+n <= 122:
#                 answer.append(chr(ord(i)+n))
#             else:
#                 answer.append(chr(ord(i)+n-26))
#     return ''.join(answer)

def solution(s, n):
    answer = list(s)
    
    for i in range(len(answer)):
        if answer[i].isupper():
            answer[i]=chr((ord(answer[i])-ord('A')+ n)%26+ord('A'))
        elif answer[i].islower():
            answer[i]=chr((ord(answer[i])-ord('a')+ n)%26+ord('a'))

    return "".join(answer)