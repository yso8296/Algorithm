def solution(n):
    result = 1
    for i in range(1, n // 2 + 1):
        sum = 0
        for j in range(i, n):
            sum += j
            if sum == n:
                result += 1
                break
            elif sum > n:
                break
    return result
            
            