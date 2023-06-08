# dp
import sys
input = sys.stdin.readline

N = int(input())
homes = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 2, -1, -1):
    for j in range(3):
        if j == 0:
            homes[i][j] += min(homes[i + 1][1], homes[i + 1][2])
        elif j == 1:
            homes[i][j] += min(homes[i + 1][0], homes[i + 1][2])
        else:
            homes[i][j] += min(homes[i + 1][0], homes[i + 1][1])

print(min(homes[0]))
        

# 첫번째 시간초과: 브루트포스
# def sol(i, j, cost):
#     if i == N:
#         return cost
    
#     result = 0

#     if j == 0:
#         result = min(
#             sol(i + 1, 1, cost + homes[i][j]),
#             sol(i + 1, 2, cost + homes[i][j])
#         )
#     elif j == 1:
#         result = min(
#             sol(i + 1, 0, cost + homes[i][j]),
#             sol(i + 1, 2, cost + homes[i][j])
#         )
#     else:
#         result = min(
#             sol(i + 1, 0, cost + homes[i][j]),
#             sol(i + 1, 1, cost + homes[i][j])
#         )
    
#     return result
    
# print(min(sol(0, 0, 0), sol(0, 1, 0), sol(0, 2, 0)))