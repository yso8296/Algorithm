n = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split())) # + - * //
max_num = -int(1e9)
min_num = int(1e9)

def calculator(num, count):
  global max_num
  global min_num
  if count == n:
    max_num = max(max_num, num)
    min_num = min(min_num, num)
    return
  if operator[0] != 0:
    operator[0] -= 1
    calculator(num + numbers[count], count + 1)
    operator[0] += 1
  if operator[1] != 0:
    operator[1] -= 1
    calculator(num - numbers[count], count + 1)
    operator[1] += 1
  if operator[2] != 0:
    operator[2] -= 1
    calculator(num * numbers[count], count + 1)
    operator[2] += 1
  if operator[3] != 0:
    operator[3] -= 1
    calculator(int(num / numbers[count]), count + 1)
    operator[3] += 1
  
calculator(numbers[0], 1)
print(max_num)
print(min_num)