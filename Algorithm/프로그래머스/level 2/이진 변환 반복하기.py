def solution(s):
    result = [0, 0]
    
    while True:
        temp = ""
        if s == "1":
            break
        s = list(s)
        result[0] += 1
        count = s.count("1")
        result[1] += s.count("0")
        cur = count
        while cur:
            temp += str(cur % 2)
            cur //= 2
        s = temp[::-1]
    return result
            
    
    