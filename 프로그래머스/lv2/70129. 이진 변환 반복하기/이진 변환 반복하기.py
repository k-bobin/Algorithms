
def solution(s):
    answer = []
    zeros, trns = 0,0
    
    while True:
        #0세기 
        zeros += s.count('0')
        #0제거
        s= s.replace('0','')
        #길이이진화
        s= bin(len(s))[2:]
        trns +=1 
        
        if s == '1':
            break
        
    return [trns, zeros]