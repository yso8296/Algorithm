def solution(s):
    result = len(s)
    for i in range(1, len(s) // 2 + 1):
        temp = ''
        cur = ''
        count = 0
        for j in range(0, len(s), i):
            if len(cur) == 0: # 처음이라면
                cur = s[j : j + i]
                count += 1
            else: # 아니라면
                if s[j : j + i] == cur:
                    count += 1
                else:
                    if count == 1:
                        temp += cur
                        cur = s[j : j + i]
                    else:
                        temp += str(count) + cur
                        count = 1
                        cur = s[j : j + i]
        if count == 1:
            temp += cur
        else:
            temp += str(count) + cur
        result = min(result, len(temp))
    
    return result
            
                
            