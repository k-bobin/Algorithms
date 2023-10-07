def solution(food):
    answer = ''
    front = ''
    for i in range(1,len(food)):
        front+= str(i)*(food[i]//2)
    
    return front+'0'+front[::-1]

