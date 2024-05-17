n = int(input())
m = int(input())
parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(1, n + 1):
  temp = list(map(int, input().split()))
  for j in range(n):
    if temp[j] == 1:
      union(i, j + 1)

plan = list(map(int, input().split()))
for i in range(len(plan)):
  for j in range(i, len(plan)):
    if find(plan[i]) != find(plan[j]):
      print("NO")
      exit()
print("YES")