from collections import deque
t = int(input())

for _ in range(t):
  result = 0
  n = int(input())
  array = list(map(int, input().split()))
  array.sort(reverse=True) 
  temp = deque()
  temp.append(array.pop())
  while True:
    temp.append(array.pop())
    if len(array) == 0:
      break
    temp.appendleft(array.pop())
    if len(array) == 0:
      break
  temp = list(temp)
  for i in range(len(temp)):
    if i != len(temp) - 1:
      result = max(result, abs(temp[i] - temp[i - 1]), abs(temp[i] - temp[i + 1]))
    else:
      result = max(result, abs(temp[i] - temp[i - 1]), abs(temp[i] - temp[0]))
  print(result)

    