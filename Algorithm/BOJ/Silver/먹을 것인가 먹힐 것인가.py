t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  a = list(map(int, input().split())) # 1 1 3 7 8
  b = list(map(int, input().split())) # 1 3 6
  a.sort()
  b.sort()
  start = 0
  num = 0
  result = 0
  for i in range(n):
    if start == m:
      result += num
      continue
    while a[i] > b[start]:
      start += 1
      num += 1
      if start == m:
        break
    result += num
  print(result)