# import sys
# input = sys.stdin.readline

# n = int(input())

# num = list(map(int, input().split()))

# count = 0
# anw = []
# for i in range(n):
#     for j in range(n):
#         if num[i] > num[j]:
#             count += 1
#         else: 
#             continue
    
#     anw.append(count)
#     count = 0

# print(*anw)

# 시간초과

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
anw = []
dp = [0] * n
count = 0
for i in range(n):
    anw.append((num[i], i))

anw.sort()

for j in range(1, n):
    if anw[j][0] != anw[j - 1][0]:
        count += 1
    dp[anw[j][1]] = count

print(dp)