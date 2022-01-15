def solution(lottos, win_nums):
    inter = set(win_nums)&set(lottos)
    min_rank = 7 - len(inter) if (7 - len(inter)) < 7 else 6
    max_rank = min_rank - lottos.count(0) if (min_rank - lottos.count(0)) > 0 else 1
    return [max_rank, min_rank]