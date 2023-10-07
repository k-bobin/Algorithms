def solution(s):
    _dict = {i:-1 for i in set(s)}
    answer = []
    for idx,letter in enumerate(s):
        if _dict[letter] == -1:
            answer.append(-1)
        else:
            answer.append(idx - _dict[letter])
        
        _dict[letter] = idx
    return answer