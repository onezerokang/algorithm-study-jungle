import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

p = list(set(permutations(nums, M)))
p.sort()

for i in range(len(p)):
    print(" ".join(map(str, p[i])))