import math
def convert_time(times):
    h,m = map(int, times.split(':'))
    return h*60 + m 

def solution(fees, records):
    answer = []
    cars = {i.split()[1]:[] for i in records}
    result = cars
    
    for i in records:
        tm, num, st = i.split()
        cars[num].append(convert_time(tm))
    
    #출차내역이 없는거  넣기 
    for k,v in cars.items():
        if len(v) % 2 == 1:
            cars[k].append(23*60+59)
    
    
    for k,v in cars.items():
        total = 0
        for m in range(1, len(v),2):
            total += v[m] - v[m-1]
        
        print(total)
        #기본 시간(분), 기본 요금(원),단위 시간(분),단위 요금(원)
        if total <= fees[0]:
            result[k] = fees[1]
        else:
            result[k] = (math.ceil((total-fees[0])/fees[2]))*fees[3] + fees[1]
    
    result = sorted(result.items(), key = lambda x:x[0])
    answer = [i[1] for i in result]
        
    return answer