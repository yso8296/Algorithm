s = input()
data = list(s)
result = 0

for i in data:
  if int(i) == 0 or int(i) == 1:
    result += int(i)
  else:
    if result <= 1:
      result += int(i)
    else:
      result *= int(i)

print(result)