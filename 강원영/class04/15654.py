import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# 순서는 상관이 있다.
nPr = list(permutations(nums, M))
for seq in nPr:
    print(" ".join(map(str, seq)))