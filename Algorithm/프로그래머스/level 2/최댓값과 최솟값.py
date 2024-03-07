def solution(s):
    array = s.split()
    for i in range(len(array)):
        array[i] = int(array[i])
    return str(min(array)) + " " + str(max(array))