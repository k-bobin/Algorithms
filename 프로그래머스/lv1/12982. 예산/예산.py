import heapq
def solution(d, budget):
    answer = 0
    heapq.heapify(d)
    
    while len(d):
        min_num = heapq.heappop(d)
        
        if min_num > budget:
            break
            
        budget -= min_num
        answer += 1 
    return answer

10
2, 8
2, 6
3, 3
3, 0