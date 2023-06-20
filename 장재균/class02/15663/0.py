# import sys
# input = sys.stdin.readline
# from itertools import permutations

# N, M = map(int, input().split())

# num = list(map(int, input().split()))

# ans = []
# for j in permutations(num, M):
#     nums = j
#     ans.append(nums)

# a = set(ans)
# b = list(a)
# sorted_lst = sorted(b, key=lambda x: (x[0], x[1]))

# for i in range(len(b)):
#     print(*sorted_lst[i])

import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())

num = list(map(int, input().split()))

ans = []
for j in permutations(num, M):
    ans.append(j)

num = list(set(ans))
num.sort()
for i in range(len(num)):
    print(*num[i])
