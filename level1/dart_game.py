def solution(dartResult):
    b = ''
    for i in dartResult:
        if i in ['S', 'D', 'T', '*', '#']:
            b += f'{i} '
        else:
            b += i
    b = b.split()
    special = {
        'S':lambda x: pow(x, 1),
        'D':lambda x: pow(x, 2),
        'T':lambda x: pow(x, 3),
        # '*':lambda x: x*2,
        # '#': lambda x: x*(-1)
        }
    for i, v in enumerate(b):
        if v not in ['*', '#']:
            b[i] = special[v[-1]](int(v[:-1]))
    for i, v in enumerate(b):
        if v == '*':
            if i-2 >= 0:
                b[i-2] *= 2
                b[i-1] *= 2
                b.pop(i)
            else:
                b[i-1] *= 2
                b.pop(i)
        if v == '#':
            b[i-1] *= -1
            b.pop(i)
    return sum(b)