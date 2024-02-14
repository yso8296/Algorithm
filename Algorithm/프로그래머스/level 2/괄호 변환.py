def balanced(p):
    u = ''
    count = 0
    idx = 0
    for i in range(len(p)):
        u += p[i]
        if p[i] == '(':
            count += 1
        if p[i] == ')':
            count -= 1
        if count == 0:
            idx = i
            break
    v = p[i + 1:]
    return u, v

def check(u):
    count = 0
    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        if u[i] == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False
    
def solution(p): 
    if p == '': #1
        return p
    if check(p):
        return p
    u, v = balanced(p) #2
    if check(u): #3
        return u + solution(v) #3-1
    else: #4
        temp = '(' #4-1
        temp += solution(v) #4-2
        temp += ')' #4-3
        for i in range(1, len(u) - 1): #4-4
            if u[i] == '(':
                temp += ')'
            if u[i] == ')':
                temp += '('
        return temp #4-5
        