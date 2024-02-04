n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
max_fear = data[0]
count = 0

for i in range(n):
  max_fear = max(max_fear, data[i])
  count += 1
  if count == max_fear:
    count = 0
    result += 1

print(result)
  