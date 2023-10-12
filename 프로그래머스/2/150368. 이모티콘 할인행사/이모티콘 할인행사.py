#3:50 ->4:37
from itertools import product
def solution(users, emoticons):
    discounts = [10,20,30,40]
    percents = [i for i in product(discounts, repeat = len(emoticons))]
    answer = []
    
    #비율 조합만들기 
    for p in percents:
        membership, bought = 0,0
        
        #한사람씩 얼마사는지 계산
        for u in users:
            limit, register_price =u
            temp = 0
            #제품 할인율 계산하여 한사람 전체 구매금액 만들기 
            for e, pp in zip(emoticons, p):
                if limit <= pp:
                    temp += e- (e//100*pp)
                    
            if register_price <= temp:
                membership += 1 
            else:
                bought += temp
        answer.append([membership, bought])

    answer.sort(key = lambda x:(x[0],x[1]))
    return answer[-1]

