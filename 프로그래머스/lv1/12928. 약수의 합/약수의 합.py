import math
def division(num):
    stack= []
    for i in range(1,int(math.sqrt(num)+1)):
        if num % i == 0:
            stack.append(i)
            if i != num//i:
                stack.append(num//i)
    return stack

def solution(n):
    return sum(division(n))