n, k = map(int, input().split())
weight = [0] * (n + 1)
value = [0] * (n + 1)
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  w, v = map(int, input().split())
  weight[i] = w
  value[i] = v

for i in range(1, n + 1):
  for j in range(1, k + 1):
    if j - weight[i] >= 0:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    else:
      dp[i][j] = dp[i - 1][j]

print(max(dp[n]))

