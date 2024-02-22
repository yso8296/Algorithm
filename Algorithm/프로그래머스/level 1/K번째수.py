def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        temp = array[i - 1 : j]
        temp.sort()
        result.append(temp[k - 1])
    return result