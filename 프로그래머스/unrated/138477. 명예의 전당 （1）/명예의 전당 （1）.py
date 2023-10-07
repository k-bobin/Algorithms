import heapq

def solution(k, score):
    answer = []
    heap = []
    l = 0
    for i in score:
        if l < k:
            l += 1
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        answer.append(heap[0])
    return answer