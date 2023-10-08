import string
import math

tmp = string.digits + string.ascii_lowercase
def convert(num,base):
    q,r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q,base) + tmp[r]
    
def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i  ==0:
            return False
    return True
    

def solution(n, k):
    answer = 0
    converted= convert(n,k)
    splited = converted.split('0')
    
    for i in splited:
        if i.isdecimal(): 
            if i != '1' and is_prime(int(i)):
                answer +=1

    return answer