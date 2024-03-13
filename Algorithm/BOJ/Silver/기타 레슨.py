n, m = map(int, input().split())
array = list(map(int, input().split()))
result = int(1e9)

def binary_search(start, end): # 9 45
  global result
  while start <= end:
    mid = (start + end) // 2
    sum = 0
    count = 1
    for i in range(len(array)):
      if sum + array[i] > mid:
        count += 1
        sum = 0
      sum += array[i]
    if count <= m:
      result = mid
      end = mid - 1
    else:
      start = mid + 1
    
binary_search(max(array), sum(array))
print(result)