n = int(input())
arr = list(map(int, input().split()))
result = [0] * n

def back(count):
  if count == n:
    for i in range(n):
      idx = result[i] - 1  # 1
      cnt = 0
      for j in range(i):
        if result[j] > result[i]:
          cnt += 1
      if cnt != arr[idx]:
        return
    for i in result:
      print(i, end=' ')
    exit()

  for i in range(n):
    if (i + 1) not in result:
      result[count] = i + 1
      back(count + 1)
      result[count] = 0

back(0)