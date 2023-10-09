import heapq
def solution(book_time):
    answer = 0
    def convert(s):
        hr,mins = map(int, s.split(':'))
        return hr*60+mins
    
    times = []
    for i in book_time:
        s,e = i
        times.append([convert(s), convert(e)])
    
    times.sort(key = lambda x:(x[0],x[1]))
    
    q = []
    #가장 빨리끝나는 애 골르기 
    for i in times:
        print(i)
        s,e = i
        if not len(q):
            heapq.heappush(q,e)
            answer +=1 
        else:
            earliest = heapq.heappop(q)
            if s < earliest + 10:
                answer += 1 
                heapq.heappush(q,e)
                heapq.heappush(q,earliest)
            else:
                heapq.heappush(q,e)
                
      
    return answer