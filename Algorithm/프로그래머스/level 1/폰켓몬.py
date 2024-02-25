def solution(nums):
    array = []
    for num in nums:
        if num not in array and len(array) < int(len(nums) / 2):
            array.append(num)
    return len(array)