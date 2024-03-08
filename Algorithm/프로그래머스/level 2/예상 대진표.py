def solution(n,a,b):      
    count = 1
    while True:
        a = (a + 1) // 2
        b = (b + 1) // 2
        if a == b:
            return count
        count += 1
        
        