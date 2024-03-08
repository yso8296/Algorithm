def solution(want, number, discount):
    result = 0
    for i in range(len(discount) - 10 + 1):
        temp = discount[i : i + 10]
        check = True
        for j in range(len(want)):
            if temp.count(want[j]) < number[j]:
                check = False
                break
        if check:
            result += 1
    return result
            