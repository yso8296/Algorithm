n = int(input())
array = list(map(int, input().split()))
result = 0
visited = [0] * n
temp = [0] * n

def dfs(count):
  global result
  if count == n:
    sum = 0
    for i in range(n - 1):
      sum += abs(temp[i] - temp[i + 1])
    result = max(result, sum)
    return
  
  for i in range(n):
    if visited[i] == 0:
      temp[count] = array[i]
      visited[i] = 1
      dfs(count + 1)
      visited[i] = 0

dfs(0)
print(result)