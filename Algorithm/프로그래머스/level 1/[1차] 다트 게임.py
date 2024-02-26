def solution(dartResult):
    score = [0, 0, 0]
    idx = 0
    for i in range(len(dartResult)):
        if '0' <= dartResult[i] <= '9':
            if dartResult[i + 1] == '0':
                score[idx] = 10
            else:
                if score[idx] == 0:
                    score[idx] = int(dartResult[i])
        if dartResult[i] == 'S':
            score[idx] = score[idx] ** 1
            if i + 1 < len(dartResult) and dartResult[i + 1] == '*':
                score[idx] *= 2
                if idx - 1 >= 0:
                    score[idx - 1] *= 2
            if i + 1 < len(dartResult) and dartResult[i + 1] == '#':
                score[idx] = -score[idx]
            idx += 1
        if dartResult[i] == 'D':
            score[idx] = score[idx] ** 2
            if i + 1 < len(dartResult) and dartResult[i + 1] == '*':
                score[idx] *= 2
                if idx - 1 >= 0:
                    score[idx - 1] *= 2
            if i + 1 < len(dartResult) and dartResult[i + 1] == '#':
                score[idx] = -score[idx]
            idx += 1
        if dartResult[i] == 'T':
            score[idx] = score[idx] ** 3
            if i + 1 < len(dartResult) and dartResult[i + 1] == '*':
                score[idx] *= 2
                if idx - 1 >= 0:
                    score[idx - 1] *= 2
            if i + 1 < len(dartResult) and dartResult[i + 1] == '#':
                score[idx] = -score[idx]
            idx += 1
    return sum(score)
        