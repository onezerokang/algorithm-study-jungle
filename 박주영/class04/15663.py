# N과 M (9)
# N개의 자연수 중에서 M개를 고르는 수열을 모두 고르시오

import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nPr = permutations(nums, M)
ans = list(set(nPr))
ans.sort()

for i in range(len(ans)):
    for j in range(M):
        print(ans[i][j], end=' ')
    print()