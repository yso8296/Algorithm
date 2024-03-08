def solution(arr):
    arr.sort()
    cur = arr[-1]
    num = 1
    while True:
        check = True
        for a in arr:
            if cur % a != 0:
                check = False
                break
        if check == True:
            return cur
        num += 1
        cur = arr[-1] * num
        
        