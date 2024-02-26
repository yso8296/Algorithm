def solution(n, losts, reserve):
    losts.sort()
    reserve.sort()
    lost_count = 0
    temp = []
    for lost in losts:
        if lost in reserve:
            reserve.remove(lost)
            temp.append(lost)
    for lost in losts:
        if lost in temp:
            continue
        if lost - 1 in reserve:
            reserve.remove(lost - 1)
        elif lost + 1 in reserve:
            reserve.remove(lost + 1)
        else:
            lost_count += 1
    return n - lost_count
        