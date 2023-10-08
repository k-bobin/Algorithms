#실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
#실패율이 높은 스테이지부터 내림차순으로 출력 
def solution(N, stages):
    answer = []
    result = {i:0 for i in range(1,N+1)}
    total = len(stages)
    

    for i in range(1,N+1):
        #x특정 스테이지에 멈춰있는 사람 수 
        temp = stages.count(i)
        if total == 0:
            result[i] = 0
        else:
            result[i] = temp/total
        total -= temp
    
    result = sorted(result.items(), key = lambda x:(-x[1],x[0]))
    
    for i in result:
        answer.append(i[0])
    return answer