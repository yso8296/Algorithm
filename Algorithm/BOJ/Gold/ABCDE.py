n, m = map(int, input().split())
graph = [[] * n for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
check = False
visited = [0] * n

def dfs(start, count):
  global check
  visited[start] = 1
  if count == 5:
    check = True
    return
  
  for i in graph[start]:
    if not visited[i]:
      dfs(i, count + 1)
  visited[start] = 0

for i in range(n):
  dfs(i, 1)
  if check:
    break

if check:
  print(1)
else:
  print(0)