n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))
num = n // 2
result = int(1e9)
visited = [False] * n

def simulate(team):
  start = []
  link = []
  start_sum = 0
  link_sum = 0
  for i in range(n):
    if team[i]:
      start.append(i)
    else:
      link.append(i)
  for i in range(num):
    for j in range(num):
      if i != j:
        start_sum += board[start[i]][start[j]] 
        link_sum += board[link[i]][link[j]]
  return abs(start_sum - link_sum)

def dfs(count, idx):
  global result
  if count == num:
    result = min(result, simulate(visited))

  for i in range(idx, n):
    if not visited[i]:
      visited[i] = True
      dfs(count + 1, i + 1)
      visited[i] = False
      
dfs(0, 0)
print(result)
