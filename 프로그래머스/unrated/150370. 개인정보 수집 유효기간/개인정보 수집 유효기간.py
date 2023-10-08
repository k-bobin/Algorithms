#모든 달은 28일까지 있다고 가정합니다.
def solution(today, terms, privacies):
    answer = []
    
    term = {}
    #months -days로 바꾸기 
    for i in terms:
        types, months = i.split()
        term[types] = int(months)*28
        
    #오늘날짜 days로 바꾸기 
    def convert_days(t):
        todays= 0 
        y,m,d = map(int, t.split('.'))
        todays +=(y-1)*28*12
        if m == 1:
            todays += d
        else:
            todays += (m-1)*28
            todays += d    
        return todays
    
    today = convert_days(today)
    
    #파기 날짜 만들기
    for idx, temp in enumerate(privacies):
        dates, t = temp.split()
        #날짜 구하기
        temp= convert_days(dates)
        temp += term[t]
        
        if temp <= today:
            answer.append(idx+1)
    
    return answer