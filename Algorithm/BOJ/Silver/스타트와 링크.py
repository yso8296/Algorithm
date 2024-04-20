n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
start = []
link = []
result = int(1e9)

def dfs(count, idx):
  global result
  if count == int(n / 2):
    start_sum = 0
    link_sum = 0
    for i in range(n):
      if i not in start:
        link.append(i)
    for i in range(int(n / 2) - 1):
      for j in range(i + 1, int(n / 2)):
        start_sum += (graph[start[i]][start[j]] + graph[start[j]][start[i]])
    for i in range(int(n / 2) - 1):
      for j in range(i + 1, int(n / 2)):
        link_sum += (graph[link[i]][link[j]] + graph[link[j]][link[i]])
    result = min(result, abs(start_sum - link_sum))
    link.clear()
    return
  
  for i in range(idx, n):
    if i not in start:
      start.append(i)
      dfs(count + 1, i + 1)
      start.pop()

dfs(0, 0)
print(result)