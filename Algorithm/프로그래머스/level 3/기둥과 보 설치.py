def check(answer):
    for x, y, a in answer:
        if a == 0: # 기둥이라면
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        elif a == 1: # 보라면
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True
    

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0: # 삭제라면
            if [x, y, a] in answer:
                answer.remove([x, y, a])
                if not check(answer):
                    answer.append([x, y, a])
            else:
                continue
        elif b == 1: # 설치라면
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
    
    answer.sort(key=lambda item: (item[0], item[1], item[2]))
    return answer