from itertools import product
def solution(numbers, target):
    answer = 0
     
    number = [(i, -i) for i in numbers]
    
    #조합 만들기 
    for i in product(*number):
        if sum(i) == target:
            answer +=1 
    return answer