t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  data = list(map(int, input().split()))
  array = [[0] * m for _ in range(n)]
  dp = [[0] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      array[i][j] = data.pop()
  for i in range(n):
    dp[i][0] = array[i][0]
  
  for i in range(1, m):
    for j in range(n):
      if j == 0:
        dp[j][i] = array[j][i] + max(dp[j][i - 1], dp[j + 1][i - 1])
      elif j == n - 1:
        dp[j][i] = array[j][i] + max(dp[j - 1][i - 1], dp[j][i - 1])
      else:
        dp[j][i] = array[j][i] + max(dp[j - 1][i - 1], dp[j][i - 1], dp[j + 1][i - 1])

  result = 0
  for i in range(n):
    result = max(result, dp[i][m - 1])
  print(result)
  