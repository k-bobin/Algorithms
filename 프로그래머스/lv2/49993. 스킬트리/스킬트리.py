def solution(skill, skill_trees):
    answer = 0
    allowed = list(skill)
    for i in skill_trees:
        s= skill
        idx = 0
        cnt = 0
        for j in i:
             if j in allowed:
                cnt +=1
                if skill[idx] == j:
                    idx +=1 
        if cnt == idx:
            answer +=1                     
                    
    return answer