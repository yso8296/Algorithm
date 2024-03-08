def solution(elements):
    array = elements * 2
    s = set(elements)
    for i in range(0, len(elements)):
        for j in range(1, len(elements) + 1):
            s.add(sum(array[i : i + j]))
    return len(s)