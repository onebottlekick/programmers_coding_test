def solution(participant, completion):
    d = {}
    hash_value = 0
    for p in participant:
        d[hash(p)] = p
        hash_value += hash(p)
    for c in completion:
        hash_value -= hash(c)
    return d[hash_value]