import sys
input = sys.stdin.readline

h,w = map(int,input().split())
height = list(map(int, (input().split())))
water = 0

for i in range(1,w-1):
    cur = height[i]
    left_wall= max(height[:i])
    right_wall= max(height[i+1:])

    if cur<left_wall and cur<right_wall:
        water += min(left_wall, right_wall) - cur
    
print(water)