def solution(s):
    s = s.strip('{{').strip('}}').replace(',{', '').replace('{', '').split('}')
    a = []
    for i in s:
        a.append(i.split(','))
    a = sorted(a, key=lambda x: len(x))
    b = []
    for i in a:
        b.append(set(i))
    c = []
    for i in range(len(b)):
        if i == 0:
            c.append(int(list(b[i])[0]))
        next_el = b[i] - b[i-1]
        if next_el != set():
            c.append(int(list(next_el)[0]))
    return c