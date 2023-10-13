#2:32
def solution(s):
    answer = 0
    cnt = 0
    stack = []
    for _ in range(len(s)):
        s = s[1:] + s[:1]
        cnt = 0
        for i in s:
            if len(stack) == 0 and (i== ']' or i== ')' or i== '}'):
                break
            elif i== '[' or i== '(' or i== '{':
                stack.append(i)
                cnt +=1 
            elif stack[-1] == '[' and i== ']':
                stack.pop()
                cnt +=1
            elif stack[-1] == '(' and i== ')':
                stack.pop()
                cnt +=1
            elif stack[-1] == '{' and i== '}':
                stack.pop()
                cnt +=1

        
        if len(stack) == 0 and cnt == len(s):
            answer +=1 
            
            
    return answer