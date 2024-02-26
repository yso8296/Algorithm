def solution(s):
    ch = s[0]
    result = 0
    original = 1
    other = 0
    for i in range(1, len(s)):
        if len(ch) == 0:
            ch = s[i]
            original = 1
            continue
        if s[i] == ch:
            original += 1
        else:
            other += 1
        if original == other:
            result += 1
            original = 0
            other = 0
            ch = ''
    if original != 0:
        result += 1
    return result