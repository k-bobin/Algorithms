def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def solution(arr):
    first = arr[0]
    for i in arr[1:]:
        first = lcm(first, i)
        
    return first
