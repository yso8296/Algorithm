from collections import deque
n, k = map(int, input().split())
visited = [0] * 200001
count = 0
time = -1

def bfs():
  global time
  global count
  q = deque()
  q.append((n, 0))
  visited[n] = 1
  while q:
    d, t = q.popleft()
    visited[d] = 1
    if time != -1:
      if t > time:
        break
    if d == k:
      count += 1
      if time == -1:
        time = t
    if d * 2 <= 200000 and not visited[d * 2]:
      q.append((d * 2, t + 1))
    if d + 1 <= 200000 and not visited[d + 1]:
      q.append((d + 1, t + 1))
    if d - 1 >= 0 and not visited[d - 1]:
      q.append((d - 1, t + 1))

bfs()
print(time)
print(count)
