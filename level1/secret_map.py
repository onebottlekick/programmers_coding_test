def solution(n, arr1, arr2):
    answer = []
    result_list = check(n, arr1, arr2)
    for result in result_list:
        answer.append(make_code(result))
    return answer
def check(n, arr1, arr2):
    a1 = []
    a2 = []
    result = []
    for _ in range(len(arr1)):
        result.append([])
    for i in arr1:
        a1.append(make_binary(i, n))
    for j in arr2:
        a2.append(make_binary(j, n))
    for i in range(len(a1)):
        for j in range(len(a1[0])):
            if int(a1[i][j]) == 1 or int(a2[i][j]) == 1:
                result[i].append('1')
            else:
                result[i].append('0')
    return result
    
def make_binary(x, n):
    x = bin(x).split('0b')[-1]
    a = x.replace('', ' ').split()
    while len(a) < n:
        a.insert(0, '0')
    return a

def make_code(a):    
    return ''.join(a).replace('0', ' ').replace('1', '#')
