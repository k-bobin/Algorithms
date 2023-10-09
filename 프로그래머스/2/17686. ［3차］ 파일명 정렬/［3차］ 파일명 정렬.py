#11:01 -> 
def solution(files):
    answer = []
    new_file = {i:0 for i in files}

    for idx, i in enumerate(files):
        stack =[]
        l,n,t = '','',''
        for j in range(len(i)):
            if not len(n):
                if i[j].isdecimal():
                    n += i[j]
                else:
                    l += i[j]
                    
            else:
                if i[j].isdecimal():
                    n+= i[j]
                else:
                    t = i[j:]
                    break
        new_file[i] = [l.lower(),int(n),idx]    
    
    sorted_file = sorted(new_file.items(), key = lambda x:(x[1][0],x[1][1],x[1][2]))

    for i in sorted_file:
        answer.append(i[0])
        
    return answer