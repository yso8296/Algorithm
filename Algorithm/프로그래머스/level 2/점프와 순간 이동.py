def solution(n):  # 5000 2500 1250 625 624 312 156 78 39 38 19 18 9 8 4 2 1 0
    count = 0
    while n:
        while n % 2 != 0:
            n -= 1
            count += 1
        n //= 2
    return count
    
        