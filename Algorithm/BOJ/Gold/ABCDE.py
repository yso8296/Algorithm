n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * n

def dfs(start, count):
  if count == 5:
    print(1)
    exit()
  
  for i in graph[start]:
    if not visited[i]:
      visited[i] = True
      dfs(i, count + 1)
      visited[i] = False

for i in range(n):
  visited = [False] * n
  visited[i] = True
  dfs(i, 1)
print(0)  
    