import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
nCr = itertools.combinations(cards, 3)

for c in nCr:
    tmp = sum(c)
    if tmp <= M and tmp > ans:
        ans = tmp

print(ans)