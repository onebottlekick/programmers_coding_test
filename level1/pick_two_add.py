def solution(numbers):
    answer = sorted(list(set([numbers[i]+numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i != j])))
    return answer

print(solution([5,0,2,7]))