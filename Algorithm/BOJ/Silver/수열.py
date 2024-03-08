n, k = map(int, input().split())
array = list(map(int, input().split()))
array = [0] + array
interval_sum = [0] * 100001
result = -int(1e9)

for i in range(1, n + 1):
  interval_sum[i] = interval_sum[i - 1] + array[i]
for i in range(1, n - k + 2):
  result = max(result, interval_sum[i + k - 1] - interval_sum[i - 1]) 
print(result)