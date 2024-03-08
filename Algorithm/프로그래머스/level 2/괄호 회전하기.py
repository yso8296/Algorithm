def solution(s):
    s = list(s)
    result = 0
    for _ in range(len(s)):
        s.append(s[0])
        s.pop(0)
        stack = []
        check = True
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    check = False
                    break
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        check = False
                        break
                if s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        check = False
                        break
                if s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        check = False
                        break
        if len(stack) > 0:
            check = False
        if check:
            result += 1
    return result
                        
        