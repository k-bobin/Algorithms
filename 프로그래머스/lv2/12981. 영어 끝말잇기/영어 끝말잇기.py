import math
def solution(n, words):
    answer = []
    used = []
    number,turn = 0,0
    
    for idx, w in enumerate(words):
        if not len(used):
            used.append(w)
        else:
            if w in used or used[-1][-1] != w[0]:
                number = idx%n+1
                turn = math.ceil((idx+1)/n)
                break
            else:
                used.append(w)
    
    return [number, turn]