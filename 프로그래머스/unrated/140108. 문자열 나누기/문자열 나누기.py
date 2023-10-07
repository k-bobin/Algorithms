def solution(s):
    answer = 1 

    f = s[0]
    f_count = 0 
    notf_count = 0 
    
    for i in s:  

        if f_count != 0 and f_count == notf_count:
            answer += 1 
            f_count = 0 
            notf_count = 0 
            f = i 

        if i == f: 
            f_count += 1
        else: 
            notf_count += 1

    return answer 