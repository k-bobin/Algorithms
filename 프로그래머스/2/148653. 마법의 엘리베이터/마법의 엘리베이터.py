def solution(storey):
    answer = 0

    while(storey!=0):
        n = storey%10
        num = 0
        if n < 5:
            num = n
            storey -= n
        elif n > 5:
            num = 10 - n
            storey += num
        else:
            num = 5


        if num == 5:
            _storey = storey // 10
            if _storey % 10 >= 5:
                storey += num
            elif _storey % 10 < 5:
                storey -= num
        storey = storey // 10
        answer += num
    return answer