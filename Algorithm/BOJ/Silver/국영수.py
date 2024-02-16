n = int(input())
data = []
for i in range(n):
  name, k, e, m = input().split()
  data.append((name, int(k), int(e), int(m)))
data.sort(key = lambda a : (-a[1], a[2], -a[3], a[0]))

for info in data:
  print(info[0])