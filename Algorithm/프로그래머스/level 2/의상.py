dic = {}

def solution(clothes):
    result = 1
    for name, cloth in clothes:
        if cloth not in dic:
            dic[cloth] = 1
        else:
            dic[cloth] += 1
    for key, value in dic.items():
        result *= value + 1
    return result - 1
        