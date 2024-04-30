n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
  parent[i] = i
result = 0
edges = []
last = 0

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

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
edges.sort()

for edge in edges:
  cost, a, b = edge
  if find(a) != find(b):
    union(a, b)
    result += cost
    last = cost

print(result - last)