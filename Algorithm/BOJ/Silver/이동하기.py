n, m =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, 1]
dy = [0, 1, 1]
dp = [[0] * m for _ in range(n)]
dp[0][0] = board[0][0]

for i in range(n):
  for j in range(m):
    for k in range(3):
      nx = i + dx[k]
      ny = j + dy[k]
      if nx >= n or ny >= m:
        continue
      dp[nx][ny] = max(dp[nx][ny], board[nx][ny] + dp[i][j])

print(dp[n - 1][m - 1])