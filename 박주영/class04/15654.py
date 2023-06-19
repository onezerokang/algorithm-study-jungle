# N과 M (5)

import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nPr = permutations(nums, M)
ans = list(set(nPr))
ans.sort()

ans_ = []
for i in range(len(ans)):
    ans_.append(list(ans[i]))
    for j in ans_[i]:
        print(j, end = ' ')
    print()