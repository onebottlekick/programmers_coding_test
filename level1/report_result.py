from collections import Counter


def solution(id_list, report, k):
    report = list(set(report))
    report_dict = {n:[] for n in id_list}
    reported = []
    for i in report:
        ke, v = i.split()
        report_dict[ke].append(v)
        reported.append(v)

    out = [a for a, b in Counter(reported).items() if b >= k]
    result = [len(set(out)&set(b)) for a, b in report_dict.items()]
    return result