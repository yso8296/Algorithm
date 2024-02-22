def solution(name, yearning, photos):
    dic = dict()
    result = []
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for photo in photos:
        sum = 0
        for p in photo:
            if p in dic:
                sum += dic[p]
        result.append(sum)
    return result
