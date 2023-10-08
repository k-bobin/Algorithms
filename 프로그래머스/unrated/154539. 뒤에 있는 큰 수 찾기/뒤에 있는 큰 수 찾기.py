
2
3
4
5
6
7
8
9
from collections import defaultdict
def solution(numbers):
    answer = [-1]*len(numbers)
    for i in range(len(numbers)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if numbers[j] >= numbers[i]:    break
            answer[j] = numbers[i]
    return answer