# 1463. 1로 만들기
# 정수 X 에 사용할 수 있는 연산은 다음과 같이 세가지이다.

# X가 3으로 나누어 떨어지면 3으로 나눔
# 2로 나누어 떨어지면 2로 나눔
# 1을 뺌

# 이 연산을 통해 1을 만들때, 연산 사용의 최솟값은?

import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0] * (N+1) # dp[i] 는 i 를 연산으로 1로 만드는데 필요한 최소 연산의 수

def oneMaker(n):
    if (n == 1):
        print(dp[1])
        return
    elif (n == 2):
        dp[2] = 1
        print(dp[2])
        return
    elif (n > 2):
        dp[2] = 1
        for i in range(3, n+1):
            if (i % 3 == 0):
                a = int(i / 3)
                c = int(i - 1)
                dp[i] = min(dp[a], dp[c]) + 1
            else:
                if (i % 2 == 0):
                    b = int(i / 2)
                    c = int(i - 1)
                    dp[i] = min(dp[b], dp[c]) + 1
                else:
                    c = int(i - 1)
                    dp[i] = dp[int(i-1)] + 1
    print(dp[n])
    return

oneMaker(N)