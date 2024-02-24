n, m = map(int, input().split())
array = []
for _ in range(n):
  array.append(int(input()))
array.sort()
dp = [int(1e9)] * 101
for num in array:
  dp[num] = 1

for i in range(n):
  for j in range(array[i], m + 1):
    dp[j] = min(dp[j], dp[array[i]] + dp[j - array[i]])

if dp[m] == int(1e9):
  print(-1)
else:
  print(dp[m])