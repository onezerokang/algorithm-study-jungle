# RGB 거리

# 집이 수직선에 존재, 집 색은 세가지, 
# 연속된 집은 같은 색이어서는 안된다. 집을 칠하는 최소비용은?

# 그리디가 아니다

# import sys
# input = sys.stdin.readline

# N = int(input().rstrip()) # 집의 수
# RGB = [None] * N # index의 집을 red, green, blue 로 칠하는 비용의 list
# dp = [0] * N # index까지 칠해진 최소 비용

# for i in range(N):
#     RGB[i] = list(map(int, input().split()))

# def min_cost(N, dp, arr):
#     dp[0] = min(arr[0])
#     pre_index = arr[0].index(dp[0])
#     for i in range(1, N):
#         a = 1000
#         index = 0
#         for j in (0, 1, 2):
#             if j == pre_index:
#                 continue
#             else:
#                 if arr[i][j] < a:
#                     a = arr[i][j]
#                     index = j
#         pre_index = index
#         print(i,'th ', 'chosen =', a)
#         dp[i] = dp[i-1]+ a
#     print(dp)

# min_cost(N, dp, RGB)

# dp, 2차원 dp 그래프를 그려보자

import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 집의 수
RGB = [None] * N # index의 집을 red, green, blue 로 칠하는 비용의 list
dp = [[0 for _ in range (3)] for _ in range(N+1)] # index까지 칠해진 최소 비용, **각 색을 선택했을 경우에**

for i in range(N):
    RGB[i] = list(map(int, input().split()))

def min_cost(N, dp, arr):
    dp[0][0] = dp[0][1] = dp[0][2] = 0

    for i in range(1, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i-1][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i-1][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i-1][2]

    print(min(dp[N]))

min_cost(N, dp, RGB)