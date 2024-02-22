def solution(numbers):
    result = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum not in result:
                result.append(sum)
    result.sort()
    return result