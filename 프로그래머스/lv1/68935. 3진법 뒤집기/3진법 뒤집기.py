import string
tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    q,r = divmod(num, base)
    if q ==0:
        return tmp[r]
    else:
        return convert(q,base)+tmp[r]
    
def solution(n):
    answer =0
    temp = convert(n, 3)
    flipped = list(reversed(str(temp)))
    nums = 1
    for i in reversed(flipped):
        answer += int(i)* nums
        nums *= 3
    return answer
