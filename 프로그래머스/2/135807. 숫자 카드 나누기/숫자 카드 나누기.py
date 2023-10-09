def gcd(a,b):
    while b >0:
        a,b =  b, a%b
    return a
    
def solution(arrayA, arrayB):
    answer = 0
    
    n = arrayA[0]
    for i in arrayA[1:]:
        n = gcd(n,i)
    
    m = arrayB[0]
    for i in arrayB[1:]:
        m = gcd(m,i)
    
    
    #a약수로 b를 나눌수 있냐?
    if all(i % n != 0 for i in arrayB):
        answer = n
    
        
    if all(i % m != 0 for i in arrayA):
        answer = max(answer, m)
    
    return answer