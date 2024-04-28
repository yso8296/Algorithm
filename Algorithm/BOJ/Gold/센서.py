n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
temp = []
for i in range(n - 1):
  temp.append(abs(arr[i] - arr[i + 1]))
temp.sort()

if k >= n:
  print(0)
  exit()
for i in range(k - 1):
  temp.pop()
print(sum(temp))