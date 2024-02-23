def solution(k, score):
    result = []
    owner = []
    for i in range(len(score)):
        if i < k:
            owner.append(score[i])
        else:
            if score[i] > owner[0]:
                owner.pop(0)
                owner.append(score[i])
        owner.sort()
        result.append(owner[0])
    return result