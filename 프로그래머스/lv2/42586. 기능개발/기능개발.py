import math 
def solution(progresses, speeds):
    answer = []
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100-p)/s))
    
    print(days)
    temp = 0
    prev = 0
    
    for d in days:
        if temp == 0:
            temp = 1 
            prev = d
            
        else:
            if prev >= d:
                temp+=1
            else:
                answer.append(temp)
                temp = 1
                prev = max(prev,d)
    
    answer.append(temp)
            
            
            
    return answer

