def solution(babbling):
    answer = 0
    letter =["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in letter:
            if j*2 in i:
                break
            else:
                i = i.replace(j," ")
        
        i = i.replace(' ','')       
        if len(i) == 0:
            answer +=1 
    return answer