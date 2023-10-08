#가짓수 (n+1)*(m+1) -1
from collections import Counter 
def solution(clothes):
    answer = 1
    _dict = {}
    for i in clothes:
        a,b =i
        if b not in _dict:
            _dict[b] = 1
        else:
            _dict[b] +=1 
    
    for i in _dict.values():
        answer *= (i+1)
        
    return answer-1
