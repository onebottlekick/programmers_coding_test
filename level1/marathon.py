def solution(participant, completion):
    dict_i = {}
    dict_j = {}
    for i in participant:
        dict_i[i] = participant.count(i)
    for j in completion:
        dict_j[j] = completion.count(j)
    print(dict_i, dict_j)
solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])