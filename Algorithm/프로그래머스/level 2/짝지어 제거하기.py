def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0 or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0
        
                
        
            