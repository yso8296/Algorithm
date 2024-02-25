def solution(k, m, score):
    count = int(len(score) / m)
    result = 0
    idx = 0
    score.sort(reverse=True)
    for _ in range(count):
        array = score[idx : idx + m]
        result += min(array) * m
        idx += m
    return result
        