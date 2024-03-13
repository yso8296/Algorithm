def solution(priorities, location):
    array = []
    count = 1
    max_priority = max(priorities)
    for i in range(len(priorities)):
        array.append(i)
    while priorities:
        idx = array.pop(0)
        priority = priorities.pop(0)
        if priority == max_priority:
            if idx == location:
                return count
            else:
                count += 1
                max_priority = max(priorities)
        else:
            priorities.append(priority)
            array.append(idx)
            
        