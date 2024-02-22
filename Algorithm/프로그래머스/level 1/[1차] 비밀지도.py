def deximal(arr, n):
    result = []
    for i in range(n):
        dex = ''
        num = arr[i]
        while num != 0:
            dex += str(num % 2)
            num //= 2
        for i in range(len(dex), n):
            dex += '0'
        dex = ''.join(reversed(list(dex)))
        result.append(dex)
    return result

def solution(n, arr1, arr2):
    result = []
    arr1 = deximal(arr1, n)
    arr2 = deximal(arr2, n)
    for i in range(n):
        word = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                word += '#'
            else:
                word += ' '
        result.append(word)
    return result
    
        