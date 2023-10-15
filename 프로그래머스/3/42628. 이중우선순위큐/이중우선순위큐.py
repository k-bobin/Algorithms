#3:16 -> 3:40 (24분)
import heapq
def solution(operations):
    answer = []
    heapq.heapify(answer)
    for i in operations:
        if len(answer) ==0 and (i =="D 1" or i =="D -1"):
            pass
        elif len(answer) != 0 and i == "D 1":
            temp = [-x for x in answer]
            heapq.heapify(temp)
            max_value = -heapq.heappop(temp)
            answer.remove(max_value)
        elif len(answer) != 0 and i == "D -1":
            heapq.heappop(answer)
        else:
            a,b = i.split()
            heapq.heappush(answer,int(b))
            
    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]