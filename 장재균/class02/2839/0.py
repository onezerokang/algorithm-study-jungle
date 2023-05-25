# import sys
# input = sys.stdin.readline

# n = int(input())

# count = 0
# while True:
#     if n >= 5:
#         count += n // 5
#         n = n % 5
#     elif n < 5 and n >= 3:
#         count += n // 3
#         n = n % 3
#     elif n == 0:
#         print(count)
#         break
#     else:
#         print(-1)
#         break
# 6, 9 예외 처리가 안되서 틀렸습니다인가...?


import sys
input = sys.stdin.readline

n = int(input())

count = 0
while n >= 0:
    if n % 5 != 0:
        n -= 3
        count += 1
    elif n % 5 == 0:
        count += n // 5
        print(count)
        break
else:
    print(-1)
# 시간 초과

# n = int(input())

# # dp[i]: i원을 거슬러주는 데 필요한 최소 동전 개수
# dp = [float('inf')] * (n + 1)
# dp[0] = 0

# coins = [3, 5]

# for coin in coins:
#     for i in range(coin, n + 1):
#         dp[i] = min(dp[i], dp[i - coin] + 1)

# if dp[n] == float('inf'):
#     print(-1)
# else:
#     print(dp[n])


# import sys
# input = sys.stdin.readline

# n = int(input())

# cnt = 0

# while n >= 0:
#     if n % 5 == 0:
#         cnt += n//5
#         print(cnt)
#         break
#     n -= 3
#     cnt += 1
# else:
#     print(-1)    
