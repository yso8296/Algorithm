step, e, w, s, n = map(int, input().split())
probability = [e, w, s, n]
visited = [(0, 0)]
result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(total, r, c):
  global result
  if len(visited) == step + 1:
    result += total
    return
  
  for i in range(4):
    nx = r + dx[i]
    ny = c + dy[i]
    if (nx, ny) in visited:
      continue
    visited.append((nx, ny))
    dfs(total * probability[i] * 0.01, nx, ny)
    visited.pop()

dfs(1, 0, 0)
print(result)
    

