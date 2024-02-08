s = input()
data = []
num = 0

for ch in s:
  if ch >= 'A' and ch <= 'Z':
    data.append(ch)
  else:
    num += int(ch)

data.sort()
result = "".join(data) + str(num)

print(result)