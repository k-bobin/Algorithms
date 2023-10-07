def solution(n, lost, reserve):
    loss = set(lost)- set(reserve)
    reserved = set(reserve) - set(lost)
    answer = 0
    for i in reserved:
        if i-1 in loss:
            answer +=1 
            loss.remove(i-1)
        elif i+1 in loss:
            answer +=1 
            loss.remove(i+1)

    return n - len(loss)