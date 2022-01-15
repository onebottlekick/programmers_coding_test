from itertools import permutations


def prime_check(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True
    
def solution(numbers):
    a = []
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            a.append(j)
    b = [int(''.join(el)) for el in set(a) if prime_check(int(''.join(el)))]
    return len(set(b))