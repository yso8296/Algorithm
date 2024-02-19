n = int(input())
dp = [[0] * 501 for _ in range(501)]

for i in range(1, n + 1):
  data = list(map(int, input().split()))
  for j in range(1, i + 1):
    dp[i][j] = data.pop()
    dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
result = 0
for i in range(1, n + 1):
  result = max(result, dp[n][i])
print(result)
