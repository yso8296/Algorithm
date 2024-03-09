def binary_search(start, end, citations):
    result = 0
    while start <= end:
        up = 0
        down = 0
        mid = (start + end) // 2
        for citation in citations:
            if citation >= mid:
                up += 1
            else:
                down += 1
        if up >= mid and down <= mid:
            result = max(result, mid)
            start = mid + 1
        else:
            end = mid - 1
    return result

def solution(citations):
    return binary_search(0, max(citations), citations)