dic = {}

def solution(players, callings):
    for i in range(len(players)):
        dic[players[i]] = i
    for calling in callings:
        idx = dic[calling]
        temp = players[idx - 1]
        dic[temp] = idx
        dic[calling] = idx - 1
        players[idx], players[idx - 1] = players[idx - 1],  players[idx]
    
    return players