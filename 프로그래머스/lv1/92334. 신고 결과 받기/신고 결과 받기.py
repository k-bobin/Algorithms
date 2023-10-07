def solution(id_list, report, k):
    answer = []
    #신고 당한 사람 중 정지당한 사람 찾기 
    _dict ={i:0 for i in id_list}
    for i in set(report):
        call, called = i.split()
        _dict[called] += 1 
    
    stopped = []
    for name, cnt in _dict.items():
        if cnt >= k:
            stopped.append(name)
            
    #캐릭터별 정지당한 사람 수 세시 
    result ={i:0 for i in id_list}
    for i in set(report):
        call, called = i.split()
        if called in stopped:
            result[call] += 1 
            
    answer = list(result.values())
    return answer