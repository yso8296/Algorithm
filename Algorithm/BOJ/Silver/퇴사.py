n = int(input())
time = []
point = []
dp = [0] * (n + 1)
max_value = 0
for _ in range(n):
  t, p = map(int, input().split())
  time.append(t)
  point.append(p)

for i in range(n - 1, -1, -1):
  if i + time[i] <= n:
    dp[i] = max(point[i] + dp[i + time[i]], max_value)
    max_value = dp[i]
  else:
    dp[i] = max_value

print(max_value)
