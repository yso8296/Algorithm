from itertools import combinations
def solution(nums):
    result = 0
    combination = list(combinations(nums, 3))
    for com in combination:
        sum = 0
        check = True
        for c in com:
            sum += c
        for i in range(2, sum):
            if sum % i == 0:
                check = False
                break
        if check:
            result += 1
    return result
    