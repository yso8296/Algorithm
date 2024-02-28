n = int(input())
array = list(map(int, input().split()))
array.reverse()
dp = [0] * n
max_value = 0

for i in range(len(array)):
  for j in range(i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp) - 1)
