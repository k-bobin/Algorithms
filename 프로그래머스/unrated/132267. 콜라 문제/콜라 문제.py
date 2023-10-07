#a: 콜라 b병얻을려면 필요한 빈명 
#b: 새콜라 
#n: 처음 가지고 있는 병 
def solution(a, b, n):
    answer = 0
    while n>= a:
        #q:새로받는 콜라, r:보유 빈병 
        q,r = divmod(n,a) #=5,0 = 10,2
        answer += q*b
        #원래가지고있는빈병-새로받긱 위해 쓴 빈병 + 새로받은 콜라(이미다마셔서 빈병)
        n = n -(q*a) + (q*b)
        
    return answer
