def solution(s):
    cur = s[0]
    arr = []
    temp = ""
    for i in range(len(s)):
        if cur == " " and s[i].isalpha():
            cur = s[i]
            arr.append(temp[0].upper() + temp[1:].lower())
            temp = s[i]
        else:
            temp += s[i]
            cur = s[i]
    arr.append(temp[0].upper() + temp[1:].lower())
    return "".join(arr)
    
         
            
        
            