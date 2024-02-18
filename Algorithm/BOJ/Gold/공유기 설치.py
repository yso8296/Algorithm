n, m = map(int, input().split())
array = []
for _ in range(n):
  array.append(int(input()))
array.sort()

def binary_search(start, end):
  result = 1
  while start <= end:
    mid = (start + end) // 2
    cur = array[0]
    count = 1
    for i in range(1, n):
      if array[i] - cur >= mid:
        count += 1
        cur = array[i]
    if count >= m:
      start = mid + 1
      result = max(result, mid)
    else:
      end = mid - 1
  return result

print(binary_search(1, array[-1] - array[0]))    



  