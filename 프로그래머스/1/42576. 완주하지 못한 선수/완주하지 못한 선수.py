from collections import Counter
def solution(participant, completion):
    answer = ''
    temp1 = Counter(participant)
    temp2 = Counter(completion)
    
    temp3 = temp1 - temp2
   
        
    return list(temp3.keys())[0]