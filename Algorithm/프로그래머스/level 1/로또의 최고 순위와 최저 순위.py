def solution(lottos, win_nums):
    result = []
    lottos.sort()
    win_nums.sort()
    zero = 0
    win = 0
    for lotto in lottos:
        if lotto in win_nums:
            win += 1
        if lotto == 0:
            zero += 1
    result.append(7 - win - zero)
    result.append(7 - win)
    if result[0] > 6:
        result[0] = 6
    if result[1] > 6:
        result[1] = 6
    return result