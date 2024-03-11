from collections import Counter

def solution(s):
    result = []
    s = s[1:-1].split('{')
    s.pop(0)
    s = "".join(s)
    s = s.split("}")
    s = "".join(s)
    s = s.split(",")
    counter = Counter(s)
    counter = counter.most_common()
    for key, value in counter:
        result.append(int(key))
    return result