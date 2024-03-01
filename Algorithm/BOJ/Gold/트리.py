n = int(input())
array = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(len(array)):
  if array[i] != -1:
    graph[array[i]].append(i)
m = int(input())
visited = [False] * n
result = 0

def remove_node(start):
  visited[start] = True
  for v in graph[start]:
    if visited[v] == False:
      remove_node(v)

def dfs(start):
  global result
  visited[start] = True
  if len(graph[start]) == 0:
    result += 1
    return
  for v in graph[start]:
    if visited[v] == False:
      dfs(v)

remove_node(m)
for i in range(len(graph)):
  if m in graph[i]:
    graph[i].remove(m)

for i in range(n):
  if visited[i] == False:
    dfs(i)

print(result)
  
