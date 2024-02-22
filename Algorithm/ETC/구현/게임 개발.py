n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]
idx = 0
count = 1
graph[x][y] = 2

def turn_left(direction):
  return (direction + 3) % 4

while True:
   d = turn_left(d) # 1
   
   nx = x + dx[d] # 2
   ny = y + dy[d]
   if graph[nx][ny] == 0:
     graph[nx][ny] = 2
     x = nx
     y = ny
     idx = 0
     count += 1
     continue
   else:
     idx += 1

   if idx == 4:
      nx = x + dx[(d + 2) % 4]
      ny = y + dy[(d + 2) % 4]
      
      if graph[nx][ny] == 2:
        x = nx
        y = ny
        idx = 0
      elif graph[nx][ny] == 1:
        break
   
print(count)