from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  st, en = map(int, input().split())
  graph[st].append(en)
visited = [-1] * (n + 1)
check = False

def bfs(start):
  visited[start] = 0
  queue = deque([start])

  while queue:
    v = queue.popleft()
    for st in graph[v]:
      if visited[st] == -1:
        visited[st] = visited[v] + 1
        queue.append(st)

bfs(x)
for i in range(1, n + 1):
  if visited[i] == k:
    print(i)
    check = True
if check == False:
  print(-1) 

