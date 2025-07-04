def solution(n, lost, reserve):
    answer = 0
    
    _reserve = sorted([r for r in reserve if r not in lost])
    _lost = sorted([r for r in lost if r not in reserve])
            
    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r + 1 in _lost:
            _lost.remove(r+1)
            
    return n - len(_lost)