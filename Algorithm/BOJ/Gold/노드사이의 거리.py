n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
visited = [0] * (n + 1)

def dfs(a, b, cost):
  visited[a] = 1
  if a == b:
    print(cost)
    return 
  
  for i in graph[a]:
    x, c = i
    if not visited[x]:
      dfs(x, b, cost + c)

for _ in range(m):
  visited = [0] * (n + 1)
  a, b = map(int, input().split())
  dfs(a, b, 0)