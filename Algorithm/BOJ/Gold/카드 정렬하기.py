import heapq
n = int(input())
data = []
for i in range(n):
  data.append(int(input()))
data.sort()
sum = 0

while True:
  a = heapq.heappop(data)
  if len(data) == 0:
    break
  b = heapq.heappop(data)
  heapq.heappush(data, a + b)
  sum += (a + b)
  
print(sum)

