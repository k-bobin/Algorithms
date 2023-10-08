from itertools import permutations
def solution(k, dungeons):
    answer = -1
    #조합만들기 
    for i in permutations(dungeons, len(dungeons)):
        energy = k
        cnt = 0
        #조합별로 탐색하기 
        for j in i:
            minv,used = j
            if energy >=minv:
                energy -= used
                cnt +=1
            else:
                break
        #지나간 단계 가장 높은걸로 업데이트하기 
        answer = max(answer, cnt)
    return answer