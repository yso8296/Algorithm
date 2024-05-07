n = int(input())
m = int(input())
parent = [0] * (n + 1)
for i in range(1, n + 1):
 parent[i] = i
networks = []
result = 0

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
  a, b, c = map(int, input().split())
  networks.append((c, a, b))
networks.sort()

for network in networks:
  cost, a, b = network
  a = find(a)
  b = find(b)
  if a != b:
    result += cost
    union(a, b)

print(result)
