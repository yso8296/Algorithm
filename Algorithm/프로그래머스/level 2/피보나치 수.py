dp = [0] * 100001
dp[1] = 1

def fibo(n):
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    return dp[n] % 1234567
        
def solution(n):
    return fibo(n)