import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
visited = [-1] * (n + 1)

def dfs(start, distance):
  for i, cost in graph[start]:
    if visited[i] == -1:
      visited[i] = distance + cost
      dfs(i, distance + cost)

visited[1] = 0
dfs(1, 0)
idx = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[idx] = 0
dfs(idx, 0)
print(max(visited))