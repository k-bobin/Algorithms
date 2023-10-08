#스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배
#아차상(#) 당첨 시 해당 점수는 마이너스된
def solution(dartResult):
    answer = 0
    points = {'S': 1 ,'D':2, 'T':3}
    
    _list =[] 
    temp = ''
    for i in dartResult:
        #숫자인경우 
        if i.isdecimal():
            temp+=i 
        #대문자일경우 
        elif i.isalpha():
            temp = int(temp)**points[i]
            _list.append(int(temp))
            temp = ''
        
        #특별부호: *
        elif i =='*':
                #하나만 존재하는경우 
            if len(_list) <2:
                _list[-1] = _list[-1] * 2       
            #두개가 존재하는경우 
            else:
                _list[-1] = _list[-1] *2
                _list[-2] = _list[-2] *2
                
        #특별부호: #
        else:
            _list[-1] = _list[-1] * -1   
            
    
        
    return sum(_list) 
