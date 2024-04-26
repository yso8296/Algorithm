n = int(input())
arr = [0]
for _ in range(n):
  num = int(input())
  arr.append(num)
result = set()
first = []
second = []

def dfs(idx, first, second):
  first.add(idx)
  second.add(arr[idx])
  if arr[idx] in first:
    if first == second:
      result.update(first)
    return
  return dfs(arr[idx], first, second)
  
for i in range(1, n + 1):
  if i not in result:
    dfs(i, set(), set())

print(len(result))
result = list(result)
result.sort()
for i in result:
  print(i)