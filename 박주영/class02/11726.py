# 2xn 타일링
# 2xn 직사각형을 1x2, 2x1타일로 채우는 방법 수를 구하는 프로그램을 작성하시오

import sys
input = sys.stdin.readline

N = int(input().rstrip())

def TwobyN(n):
    dp = [0 for i in range(1001)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 1001):
        dp[i] = (dp[i-2] + dp[i-1]) % 10007
    print(dp[n])

TwobyN(N)