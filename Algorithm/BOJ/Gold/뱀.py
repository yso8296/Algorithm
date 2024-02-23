n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
array = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
  x, y = map(int, input().split())
  array[x][y] = 1
l = int(input()) 
info = [] # 뱀의 방향 변환 정보
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [ 0, 1, 0, -1]
array[1][1] = 2
dir = 1
x = 1
y = 1
time = 0
body_info = []
body_info.append((1, 1))

while True:
  time += 1
  nx = x + dx[dir]
  ny = y + dy[dir]
  if nx < 1 or nx > n or ny < 1 or ny > n:
    break
  if array[nx][ny] == 2:
    break
  if array[nx][ny] == 1:
    array[nx][ny] = 2
    x = nx
    y = ny
    body_info.append((x, y))
  else:
    a, b = body_info.pop(0)
    array[a][b] = 0
    array[nx][ny] = 2
    x = nx
    y = ny
    body_info.append((x, y))
  if len(info) != 0:
    t, d = info[0]
    if t == time:
      if d == 'L':
        dir = (dir + 3) % 4
      if d == 'D':
        dir = (dir + 1) % 4
      info.pop(0)
  
print(time)
