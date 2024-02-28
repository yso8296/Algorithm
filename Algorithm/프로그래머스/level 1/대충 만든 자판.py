def solution(keymaps, targets):
    result = []
    dic = dict()
    for i in range(26):
        dic[chr(ord('A') + i)] = 101
    for keymap in keymaps:
        for i, key in enumerate(keymap, start = 1):
            dic[key] = min(dic[key], i)
    
    for target in targets:
        sum = 0
        check = True
        for t in target:
            if dic.get(t) == 101:
                check = False
                break
            sum += dic[t]
        if check == True:
            result.append(sum)
        else:
            result.append(-1)
    return result
        
        