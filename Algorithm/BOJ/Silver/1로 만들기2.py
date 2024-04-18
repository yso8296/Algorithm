n = int(input())
dp = [0] * 1000001
before = [0] * 1000001
dp[2] = 1
dp[3] = 1
before[2] = 1
before[3] = 1

for i in range(4, n + 1):
  num = i - 1
  dp[i] = dp[i - 1]
  if i % 2 == 0:
    if dp[i // 2] < dp[i]:
      num = i // 2
      dp[i] = dp[i // 2]
  if i % 3 == 0:
    if dp[i // 3] < dp[i]:
      num = i // 3
      dp[i] = dp[i // 3]
  dp[i] += 1
  before[i] = num

print(dp[n])
idx = n
while idx > 0:
  print(idx, end=' ')
  idx = before[idx]