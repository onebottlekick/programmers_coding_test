def solution(price, money, count):
    a = 0
    for i in range(1, count+1):
        a += price*i
    if a <= money:
        return 0
    return a - money