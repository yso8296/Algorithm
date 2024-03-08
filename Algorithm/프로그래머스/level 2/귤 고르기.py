def solution(k, tangerine):
    result = 0
    array = [0] * (max(tangerine) + 1)
    for t in tangerine:
        array[t] += 1
    array.sort()
    while True:
        result += 1
        k -= array.pop()
        if k <= 0:
            return result
    