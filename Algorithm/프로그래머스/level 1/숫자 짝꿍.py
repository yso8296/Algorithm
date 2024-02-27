def solution(X, Y):
    dic = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}
    for ch in X:
        dic[ch] += 1
    array = []
    check = False
    for ch in Y:
        if dic[ch] > 0:
            if ch != '0':
                check = True
            array.append(ch)
            dic[ch] -= 1
    if len(array) == 0:
        return "-1"
    elif check == False:
        return "0"
    else:
        array.sort(reverse=True)
        return "".join(array)
    