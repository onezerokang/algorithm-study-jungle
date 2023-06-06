from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

hq = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heappop(hq) if hq else 0)
    else:
        heappush(hq, x)