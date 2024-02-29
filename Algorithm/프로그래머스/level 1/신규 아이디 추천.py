def solution(id):
    # 1단계
    id = id.lower() 
    new_id = list(id)
    #2단계
    for i in range(len(new_id)):
        if 'a' <= new_id[i] <= 'z':
            continue
        if '0' <= new_id[i] <= '9':
            continue
        if new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            continue
        new_id[i] = ''
    new_id = list("".join(new_id))
    #3단계
    count = 0
    for i in range(len(new_id)):
        if new_id[i] == '.':
            if count == 1:
                new_id[i] = ''
            else:
                count = 1
        else:
            count = 0
    new_id = list("".join(new_id))
    #4단계
    if new_id[0] == '.':
        new_id[0] = ''
    if new_id[-1] == '.':
        new_id[-1] = ''
    new_id = list("".join(new_id))
    #5단계
    if len(new_id) == 0:
        new_id = ['a']
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id[-1] = ''
        new_id = list("".join(new_id))
    #7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
    
    return "".join(new_id)
            
                
    