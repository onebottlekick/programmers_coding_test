def solution(n, m):
    n_divisors = [i for i in range(1, n+1) if n%i==0]
    m_divisors = [j for j in range(1,m+1) if m%j==0]
    CD = [i for i in n_divisors for j in m_divisors if i==j]
    GCD = max(CD)
    n_multiples = [n*k for k in range(1, max(n,m)+1)]
    m_multiples = [m*k for k in range(1, max(n,m)+1)]
    CM = [i for i in n_multiples for j in m_multiples if i==j]
    LCM = min(CM)
    answer = []
    answer.append(GCD)
    answer.append(LCM)
    return answer

print(solution(3,12))