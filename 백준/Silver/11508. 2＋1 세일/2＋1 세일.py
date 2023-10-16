import sys
input = sys.stdin.readline

n=int(input()) 
prices =[int(input()) for _ in range(n)]
prices.sort(reverse = True)

idx = 2
for _ in range((n//3)):
    prices[idx] = 0
    idx += 3

print(sum(prices))
