def solution(s):
    check = 0
    for i in s:
        if i == '(':
            check += 1
        if i == ')':
            check -= 1
        if check == -1:
            return False
    if check == 0:
        return True
    else:
        return False
    