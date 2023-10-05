from collections import deque
a, p = map(int, input().split())

#부분 수열 만들기 
d = []
d.append(a)

while True:
    a = d[-1]
    temp= 0 
    for i in str(a):
        temp += int(i)**p

    if temp not in d:
        d.append(temp)
    else:
        break


print(d.index(temp))