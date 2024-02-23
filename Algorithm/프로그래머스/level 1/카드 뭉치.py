def solution(cards1, cards2, goal):
    first = 0
    second = 0
    first_check = True
    second_check = False
    result = []
    for i in range(len(goal)):
        if first < len(cards1):
            if cards1[first] == goal[i]:
                result.append(cards1[first])
                first += 1
        if second < len(cards2):
            if cards2[second] == goal[i]:
                result.append(cards2[second])
                second += 1
    if result == goal:
        return "Yes"
    else:
        return "No"