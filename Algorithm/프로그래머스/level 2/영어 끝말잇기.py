def solution(n, words):
    result = [0, 0]
    array = []
    order = [i for i in range(1, n + 1)]
    idx = 0
    for i, word in enumerate(words):
        if len(array) == 0:
            array.append(word)
            idx += 1
            continue
        if word not in array and word[0] == array[-1][-1]:
            array.append(word)
            idx += 1
        else:
            return [order[idx % n], idx // n + 1]
    return [0, 0]
        