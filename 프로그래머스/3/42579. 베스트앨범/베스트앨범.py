#2:32
# 리스트순서: 고유번호, 재생수
# 장르 재생수가 많은건 1번  적은거 2번 .. 
# 장르, 재생수, 고유번호
def solution(genres, plays):
    answer = []     
    _list = [[idx, num] for idx, num in enumerate(plays)]
    
    _dict = {i: 0 for i in set(genres)}
    for a,b in zip(genres, plays):
        _dict[a] += b
        
    for g,i in zip(genres, _list):
        idx, num = i
        temp = _dict[g]
        _list[idx].append(temp)
        
    print(_list)
    _list.sort(key = lambda x:(x[2],x[1],-x[0]), reverse=True)
    
    num, cnt = 0, 0 
    
    for i in _list:
        a,b,c = i
        if num != c:
            cnt = 0
            num = c
            
        if cnt <2:
            answer.append(a)
            cnt += 1 

    return answer
   