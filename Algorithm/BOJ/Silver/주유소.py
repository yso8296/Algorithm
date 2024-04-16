n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
cur_cost = cost[0]
result = 0

for i in range(n - 1):
  if cur_cost > cost[i]:
    cur_cost = cost[i]
  result += cur_cost * distance[i]

print(result)