n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dx = [-1, -1, 1, 1] # 대각선 채우기 용
dy = [-1, 1, 1, -1]
move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)] # 이동 용
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

def move_cloud(cloud_x, cloud_y, d, s):
  nx = cloud_x + move[d - 1][0] * (s % n)
  ny = cloud_y + move[d - 1][1] * (s % n)
  if nx < 0:
    nx = n + nx
  else:
    nx = nx % n
  if ny < 0:
    ny = n + ny
  else:
    ny = ny % n
  return (nx, ny)

for _ in range(m):
  d, s = map(int, input().split())
  #1,2 구름 이동 및 물 1 증가
  move_clouds = []
  for cloud in clouds: 
    cloud_x, cloud_y = cloud[0], cloud[1]
    nx, ny = move_cloud(cloud_x, cloud_y, d, s)
    graph[nx][ny] += 1
    move_clouds.append((nx, ny))
  #4 대각선 방향 물 주기
  for cloud in move_clouds:
    for i in range(4):
      nx = cloud[0] + dx[i]
      ny = cloud[1] + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0:
        continue
      graph[cloud[0]][cloud[1]] += 1
  #5 구름 생성 및 물의 양 2 감소시키기
  new_clouds = []
  for i in range(n):
    for j in range(n):
      if graph[i][j] >= 2 and (i, j) not in move_clouds:
        graph[i][j] -= 2
        new_clouds.append((i, j))
  clouds = new_clouds

sum = 0
for i in range(n):
  for j in range(n):
    sum += graph[i][j]

print(sum)
      
  
