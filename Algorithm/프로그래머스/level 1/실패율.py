# 정답은 맞췄으나 좀 더 효율적으로 코드를 짜보면 좋을 것 같다
def solution(n, stages):
    result = []
    fail = []
    stages.sort() # [1, 2, 2, 2, 3, 3, 4, 6]
    idx = 0
    people = len(stages)
    for i in range(1, n + 1):
        no_clear = 0
        num = 0
        for j in range(idx, len(stages)):
            if stages[j] == i:
                idx += 1
                num += 1
                no_clear += 1
        if people == 0:
            fail.append((i, 0))
        else:
            fail.append((i, no_clear / people))
        people -= num
    fail.sort(key = lambda a : (-a[1], a[0]))
    for i in fail:
        result.append(i[0])
    return result
                
            