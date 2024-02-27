def solution(number, limit, power):
  array = [0] * (number + 1)
  for i in range(1, number + 1):
    for j in range(1, int(number**(1/2)) + 1):
      if i % j == 0:
        array[i] += 1
        if j != int(i / j):
          array[i] += 1
    if array[i] > limit:
      array[i] = power
  return sum(array)