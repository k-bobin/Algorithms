import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [-work for work in works]  # 최대 힙을 사용하기 위해 음수로 변환
    heapq.heapify(works)

    while n > 0:
        max_work = heapq.heappop(works)
        max_work += 1
        heapq.heappush(works, max_work)
        n -= 1

    answer = sum([work ** 2 for work in works])
    return answer





