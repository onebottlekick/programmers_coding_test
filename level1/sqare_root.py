import math

def solution(n):
    return (math.sqrt(n)+1)**2 if n%math.sqrt(n)==0 else -1