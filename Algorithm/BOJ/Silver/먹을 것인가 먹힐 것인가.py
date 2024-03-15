t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  arr1 = list(map(int, input().split()))
  arr2 = list(map(int, input().split()))
  arr1.sort() # 1 1 3 7 8
  arr2.sort() # 1 3 6
  start = 0
  count = 0
  for i in range(n):
    while True:
      if start == m or arr1[i] <= arr2[start]:
        count += start
        break
      else:
        start += 1
  print(count)
    

