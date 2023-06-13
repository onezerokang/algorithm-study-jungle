# 구간 합 구하기 5

# 시간 초과

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# matrix = [list(map(int, input().split())) for _ in range(N)]
# points = [list(map(int, input().split())) for _ in range(M)]

# dp = [([0] * N) for _ in range(N)]
# for i in range(N):
#     dp[i][0] = matrix[i][0]
#     for j in range(N):
#         if j == 0:
#             continue
#         dp[i][j] = dp[i][j-1] + matrix[i][j]
# # print(points)

# for i in range(M):
#     ans = 0
#     x1 = points[i][0]-1
#     y1 = points[i][1]-1
#     x2 = points[i][2]-1
#     y2 = points[i][3]-1
#     # print('point1, ', x1, y1)
#     # print('point2, ', x2, y2)
#     # print(dp)
#     if x1 == x2 and y1 == y2:
#         print(matrix[x1][y1])
#         continue
#     for j in range(y1, y2+1):
#         if x1 == 0:
#             ans += dp[j][x2]
#             continue
#         ans += dp[j][x2] - dp[j][x1-1]
#     print(ans)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)] #구간합
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])