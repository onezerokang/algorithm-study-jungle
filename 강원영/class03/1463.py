import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

# dp[i]는 i를 1로 만들기 위한 연산의 개수
# i가 3으로 나눠지면 dp[i] = dp[i / 3] + 1
# i가 2로 나눠지면 dp[i] = dp[i / 2] + 1
# 비교 dp[i] = dp[i - 1] + 1

# 무조건 3으로 나누는게 더 좋은 것이 아니다.
# 반례: 642

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

print(dp[N])