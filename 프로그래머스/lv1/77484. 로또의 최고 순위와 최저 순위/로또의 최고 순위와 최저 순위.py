def solution(lottos, win_nums):
    #1개 이하면 6등 
    rank = {6:1, 5:2 , 4:3, 3:4, 2:5}
    answer = []
    minv, maxv = 0,0
    for i in lottos:
        if i in win_nums:
            minv +=1 
            maxv +=1 
        elif i == 0:
            maxv += 1
            
    if maxv < 2:
        answer.append(6)
    else:
        answer.append(rank[maxv])
        
    if minv < 2:
        answer.append(6)
    else:
        answer.append(rank[minv])
        
    return answer