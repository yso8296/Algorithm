def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    result = 0
    for babl in babbling:
        temp = ''
        duplicate = ''
        for alp in babl:
            temp += alp
            if temp in word:
                if temp == duplicate:
                    break
                duplicate = temp
                temp = ''
        if len(temp) == 0:
            result += 1
    return result
            
        