n, k = map(int, input().split())
array = list(map(int, input().split()))
result = 0
start = 0
end = 0
dic = {}

while end < len(array):
  if array[end] not in dic:
    dic[array[end]] = 1
    end += 1
  elif dic[array[end]] <= k:
    dic[array[end]] += 1
    end += 1
  while dic[array[end - 1]] > k:
    dic[array[start]] -= 1
    start += 1
  result = max(result, end - start)

print(result)