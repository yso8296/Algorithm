n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = board[0][0]
for i in range(n):
  for j in range(n):
    if i == 0 and j == 0:
      continue
    if i == 0:
      dp[i][j] = dp[i][j - 1] + board[i][j]
    elif j == 0:
      dp[i][j] = dp[i - 1][j] + board[i][j]
    else:
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i][j]



for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  result = 0
  if x1 == 1 and y1 == 1 and x2 == 1 and y2 == 1:
    print(dp[0][0])
    continue
  if x1 - 2 < 0 and y1 - 2 < 0:
    result = dp[x2 - 1][y2 - 1]
  elif x1 - 2 < 0:
    result = dp[x2 - 1][y2 - 1] - dp[x2 - 1][y1 - 2]
  elif y1 - 2 < 0:
    result = dp[x2 - 1][y2 - 1] - dp[x1 - 2][y2 - 1]
  else:
    result = dp[x2 - 1][y2 - 1] - dp[x1 - 2][y2 - 1] - dp[x2 - 1][y1 - 2] + dp[x1 - 2][y1 - 2]
  print(result)

  