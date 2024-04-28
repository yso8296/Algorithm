n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
  a, b = map(int ,input().split())
  graph[a].append(b)
big = [0] * (n + 1)
small = [0] * (n + 1)

def dfs(num, idx):
  visited[idx] = 1
  for i in graph[idx]:
    if not visited[i]:
      big[num] += 1
      small[i] += 1
      dfs(num, i)

for i in range(1, n + 1):
  visited = [0] * (n + 1)
  dfs(i, i)
for i in range(1, n + 1):
  print(n - big[i] - small[i] - 1)
