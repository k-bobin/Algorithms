#2:15 -> 2:27
def solution(ingredient):
    answer = 0
    stack = [] 
    if len(ingredient) <4:
        answer = 0
    elif len(ingredient) ==4 and ingredient == [1,2,3,1]:
        answer =1 
    else:
        for i in ingredient:
            stack.append(i)
            
            if stack[-4:] == [1,2,3,1]:
                for _ in range(4):
                    stack.pop()
                    
                answer += 1
    return answer