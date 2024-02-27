def solution(participants, completions):
    dic = {i:0 for i in completions}
    dic2 = {i:0 for i in participants}
    for participant in participants:
        dic2[participant] += 1
    for completion in completions:
        dic[completion] += 1
    for participant in participants:
        if dic.get(participant) == None:
            return participant
        if dic2[participant] > dic[participant]:
            return participant