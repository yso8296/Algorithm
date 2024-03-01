def solution(surveys, choices):
    result = ""
    score = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for i, survey in enumerate(surveys):
        first = survey[0]
        second = survey[1]
        if 1 <= choices[i] <= 3:
            score[first] += 4 - choices[i]
        else:
            score[second] += choices[i] - 4
    if score['R'] >= score['T']:
        result += 'R'
    else:
        result += 'T'
    if score['C'] >= score['F']:
        result += 'C'
    else:
        result += 'F'
    if score['J'] >= score['M']:
        result += 'J'
    else:
        result += 'M'
    if score['A'] >= score['N']:
        result += 'A'
    else:
        result += 'N'
    return result
    