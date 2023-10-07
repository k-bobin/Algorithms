import string
def solution(s, skip, index):
    letters = list(string.ascii_lowercase)
    
    #여기 중요
    for i in skip:
        letters.remove(i)
    
    answer = ''
    for i in s:
        temp= letters.index(i) + index
        answer += letters[temp % (26-len(skip))]
        
    return answer