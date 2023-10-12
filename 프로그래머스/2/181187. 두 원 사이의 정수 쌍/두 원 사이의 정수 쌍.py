#1:54 -> 
# def solution(r1, r2):
#     if r2 == 1:
#         temp2 = 4
#     else:
#         temp2 = (((r2-1)*2)+1)**2
    
#     if r1 ==1:
#         temp1 = 0
#     else:
#         temp1 = (((r1-1)*2)+1)**2

#     return temp2-temp1+4

def solution(r1, r2):
    import math
    # 가능한 정수 좌표 개수 초기화
    count = 0

    # x1부터 x2까지 가능한 모든 x좌표에 대해 계산
    for x in range(-r2, r2 + 1):
        # 각 x좌표에 대해 y좌표 계산

        #1. x < -r1 또는 x > r1 일 때
        if x + r1 < 0 or x - r1 > 0:

            #큰 원만 고려하여 계산
            y2_max = (r2**2 - x**2)**(1/2)
            y2_min = -y2_max

            count += math.floor(y2_max) - math.ceil(y2_min) + 1

        #2. x = -r1 또는 x = r1일때
        elif x == r1 or x == -r1:

            # 큰 원만 고려한 값 - 1
            y2_max = (r2**2 - x**2)**(1/2)
            y2_min = -y2_max

            count += math.floor(y2_max) - math.ceil(y2_min) + 1

        #3. 그 외의 경우: 큰 원 - 작은 원
        else:
            y2_max = (r2**2 - x**2)**(1/2)
            y2_min = -y2_max
            y1_max = (r1**2 - x**2)**(1/2)
            y1_min = -y1_max

            count += (math.floor(y2_max) - math.ceil(y1_max) + 1 ) + (math.floor(y1_min) - math.ceil(y2_min) + 1 )

    return count