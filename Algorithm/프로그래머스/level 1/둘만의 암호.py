def solution(s, skip, index):
    alp = [i for i in range(26)]
    for i in index:
        alp.pop(ord(i) - ord('a'))
    result = ''
    for i in s:
        result += chr(((ord(i) + (index % (len(alp - len(skip))))))) 
    return result