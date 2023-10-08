#앞뒤

def solution(survey, choices):
    
    points = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    answer = ''
    
    #각 지표별 점수 
    first = {'R':0, 'T':0}
    second ={'C':0, 'F':0}
    third = {'J':0, 'M':0}
    fourth = {'A':0, 'N':0}
    
    #설문조사 총합 만들기 
    for pairs, num in zip(survey, choices):
        #앞뒤 가르기 
        a,b = pairs.strip()
        if a in first:
            if num<4:
                first[a] += points[num]
            elif num > 4:
                first[b] += points[num]
            else: 
                pass 
            
        elif a in second:
            if num<4:
                second[a] += points[num]
            elif num > 4:
                second[b] += points[num]
            else: 
                pass
            
        elif a in third:
            if num<4:
                third[a] += points[num]
            elif num > 4:
                third[b] += points[num]
            else: 
                pass
        else:
            if num<4:
                fourth[a] += points[num]
            elif num > 4:
                fourth[b] += points[num]
            else: 
                pass
    
    f = sorted(list(first.items()), key = lambda x:(-x[1],x[0]))
    s = sorted(list(second.items()), key = lambda x:(-x[1],x[0]))
    t = sorted(list(third.items()), key = lambda x:(-x[1],x[0]))
    ff = sorted(list(fourth.items()), key = lambda x:(-x[1],x[0]))
    

    answer += f[0][0]
    answer += s[0][0]
    answer += t[0][0]
    answer += ff[0][0]
    



        
    return answer