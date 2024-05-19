n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth.pop(0)
parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i
party = []
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

if len(truth) >= 2:
  for i in range(len(truth) - 1):
    union(truth[i], truth[i + 1])

for _ in range(m):
  temp = list(map(int, input().split()))
  temp.pop(0)
  party.append(temp)
  for i in range(len(temp) - 1):
    union(temp[i], temp[i + 1])

for i in range(len(party)):
  check = True
  if len(truth) > 0:
    for j in range(len(party[i])):
      if find(truth[0]) == find(party[i][j]):
        check = False
        break
  if check:
    result += 1

print(result)
