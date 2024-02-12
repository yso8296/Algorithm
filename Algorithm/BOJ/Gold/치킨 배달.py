from itertools import combinations
n, m = map(int, input().split())
array = []
for _ in range(n):
  array.append(list(map(int, input().split())))
home = []
chicken = []
result = 1e9
for i in range(n):
  for j in range(len(array[0])):
    if array[i][j] == 1:
      home.append((i, j))
    if array[i][j] == 2:
      chicken.append((i, j))

choices = list(combinations(chicken, m))
for choice in choices:
  dist = 0
  for hx, hy in home:
    temp = 1e9
    for cx, cy in choice:
      temp = min(temp, abs(hx - cx) + abs(hy - cy))
    dist += temp
  result = min(result, dist)

print(result)
      



