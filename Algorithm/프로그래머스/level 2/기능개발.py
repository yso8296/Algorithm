from collections import deque
def solution(progresses, speeds):
    result = []
    progress = deque()
    min_idx = 1
    for i, p in enumerate(progresses, start=1):
        progress.append((i, p))
    while progress:
        idx, prog = progress[0]
        speed = speeds[0]
        if prog < 100 or idx != min_idx:
            progress.append((idx, prog + speed))
            speeds.append(speed)
            progress.popleft()
            speeds.pop(0)
        else:
            sum = 0
            while progress:
                idx, prog = progress[0]
                if idx == min_idx and prog >= 100:
                    progress.popleft()
                    speeds.pop(0)
                    min_idx += 1
                    sum += 1
                else:
                    break
            if sum != 0:
                result.append(sum)
    return result
            
            