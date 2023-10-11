import sys
from math import factorial

t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    maxv = max(n,m)
    minv = min(n,m)

    print(factorial(maxv)//(factorial(minv)*factorial(maxv-minv)))