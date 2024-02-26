def solution(n, m, section):
    result = 1
    cur = section[0]
    for i in range(1, len(section)):
        if section[i] - cur > m - 1:
            result += 1
            cur = section[i]
    return result
        