def solution(elements):  
    answer = []
    for i in range(1,len(elements)+1):
        elements = elements[1:]+elements[:1]
        for j in range(1,len(elements)+1):
            answer.append(sum(elements[:j]))
    return len(set(answer))