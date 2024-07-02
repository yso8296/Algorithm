r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
result = 0
r -= 1
c -= 1

for _ in range(101):
  if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
    print(result)
    exit()

  rmode = 1
  if len(arr) < len(arr[0]):
    rmode = 0

  if rmode == 0:  # [1] rmode가 0이면 전치행렬로 변경
    arr = list(map(list, zip(*arr)))  
  
  maxcol = 0
  for i in range(len(arr)):  # [2] 한 행씩 연산
    dict = {}
    new_arr = []
    for j in range(len(arr[i])):
      if arr[i][j] == 0:
        continue
      if arr[i][j] in dict:
        dict[arr[i][j]] += 1
      else:
        dict[arr[i][j]] = 1
    dict = sorted(dict.items(), key=lambda x : (x[1], x[0]))
    
    for d in dict:
      new_arr.append(d[0])
      new_arr.append(d[1])
    arr[i] = new_arr
    maxcol = max(maxcol, len(new_arr))
  maxcol = min(maxcol, 100)

  for i in range(len(arr)):
    while len(arr[i]) < maxcol:
      arr[i].append(0)
    while len(arr[i]) > maxcol:
      arr[i].pop()
  
  if rmode == 0: #[3] 복구
    arr = list(map(list, zip(*arr)))  
  if len(arr) > 100:
    arr = arr[:100]
  result += 1
  
print(-1)
  
  